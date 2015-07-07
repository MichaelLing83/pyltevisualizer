from .Matrix import Matrix
from .Enums import DUPLEX_MODE, BW, SF_TYPE, RE_TYPE, ANTENNA_PORTS_COUNT
from ..c6 import N_DL_symb, csrs_ap, pss_n_s_l, sss_n_s_l, pss_k_list, pss_k_reserved_list, sss_k_list, sss_k_reserved_list, is_csrs_reserved, pbch_n_s_l, pbch_k_list
from ..c4 import subframe_assignment, symbol_nr_DwPTS, symbol_nr_UpPTS, symbol_nr_GP
from ..c5 import N_UL_symb
from .Re import Re
from ..L1Config import L1Config
import logging

class Frame(Matrix):
    def __init__(self, l1_config):
        assert isinstance(l1_config, L1Config), "must be L1Config"
        self.l1_config = l1_config
        if self.l1_config.duplexMode == DUPLEX_MODE.TDD:
            assert self.l1_config.dl_bandwidth == self.l1_config.ul_bandwidth, "TDD must have the same bandwidth for DL and UL!"
            dl_cp = self.l1_config.dl_cyclicPrefixLength
            ul_cp = self.l1_config.ul_cyclicPrefixLength
            delta_f = self.l1_config.delta_f
            ssp = self.l1_config.specialSubframePatterns
            sfa = l1_config.subframe_assignment
            __size_y = BW.toReNumber(self.l1_config.dl_bandwidth, dl_cp, delta_f)
            total_DL_symbols = N_DL_symb(dl_cp, delta_f) * 2 * subframe_assignment(sfa).count(SF_TYPE.D)
            total_UL_symbols = N_UL_symb(ul_cp) * 2 * subframe_assignment(sfa).count(SF_TYPE.U)
            total_dwpts_symbols = symbol_nr_DwPTS(ssp, dl_cp, delta_f) * subframe_assignment(sfa).count(SF_TYPE.S)
            # GP is treated as one symbol
            total_gp_symbols = symbol_nr_GP(ssp, dl_cp, ul_cp, delta_f) * subframe_assignment(sfa).count(SF_TYPE.S)
            assert total_gp_symbols >= 1
            total_uppts_symbols = symbol_nr_UpPTS(ssp, dl_cp, ul_cp) * subframe_assignment(sfa).count(SF_TYPE.S)
            __size_x = total_DL_symbols + total_UL_symbols + total_dwpts_symbols + total_gp_symbols + total_uppts_symbols
        else:
            assert False, "FDD is not supported yet!"
        super().__init__(__size_x, __size_y, Re)
        # mark RE types
        self.__mark_all()
    def slot(self, index):
        '''
        Return: slot instance
        '''
        assert 0 <= index <= 20
        start_index = 0
        sfa = subframe_assignment(self.l1_config.subframe_assignment)
        dl_cp = self.l1_config.dl_cyclicPrefixLength
        ul_cp = self.l1_config.ul_cyclicPrefixLength
        delta_f = self.l1_config.delta_f
        for i in range(index):
            if sfa[int(i/2)] == SF_TYPE.D:
                start_index += N_DL_symb(dl_cp, delta_f)
            elif sfa[int(i/2)] == SF_TYPE.U:
                start_index += N_UL_symb(ul_cp)
            else:
                # special subframe
                start_index += N_DL_symb(dl_cp, delta_f)
        length = 0
        if sfa[int(index/2)] == SF_TYPE.D:
            length = N_DL_symb(dl_cp, delta_f)
        elif sfa[int(index/2)] == SF_TYPE.U:
            length = N_UL_symb(ul_cp)
        else:
            length = N_DL_symb(dl_cp, delta_f)
        slot = self[start_index:start_index+length]
        return slot
    def nr_of_DL(self):
        '''
        Return: number of DL subframes
        '''
        return subframe_assignment(self.l1_config.subframe_assignment).count(SF_TYPE.D) * 2
    def slot_DL(self, index):
        '''
        index: index out of all DL subframes in this frame

        return: slot instance, n_s
        '''
        assert 0 <= index < self.nr_of_DL()
        sfa = subframe_assignment(self.l1_config.subframe_assignment)
        dl_slot_count = 0
        for slot_index in range(20):
            if sfa[int(slot_index/2)] == SF_TYPE.D:
                if dl_slot_count == index:
                    break;
                else:
                    dl_slot_count += 1
        dl_slot = self.slot(slot_index)
        return dl_slot, slot_index
    def nr_of_UL(self):
        '''
        Return: number of UL subframes
        '''
        return subframe_assignment(self.l1_config.subframe_assignment).count(SF_TYPE.U) * 2
    def slot_UL(self, index):
        '''
        index: index out of all UL subframes in this frame

        return: slot instance, n_s
        '''
        assert 0 <= index < self.nr_of_UL()
        sfa = subframe_assignment(self.l1_config.subframe_assignment)
        ul_slot_count = 0
        for slot_index in range(20):
            if sfa[int(slot_index/2)] == SF_TYPE.U:
                if ul_slot_count == index:
                    break;
                else:
                    ul_slot_count += 1
        ul_slot = self.slot(slot_index)
        return ul_slot, slot_index
    def nr_of_GP(self):
        sfa = subframe_assignment(self.l1_config.subframe_assignment)
        return sfa.count(SF_TYPE.S)
    def slot_GP(self, index):
        '''
        Return: slot instance, n_s
        '''
        assert 0 <= 0 < self.nr_of_GP()
        start_index = 0
        dl_cp = self.l1_config.dl_cyclicPrefixLength
        ul_cp = self.l1_config.ul_cyclicPrefixLength
        delta_f = self.l1_config.delta_f
        ssp = self.l1_config.specialSubframePatterns
        sfa = subframe_assignment(self.l1_config.subframe_assignment)
        special_subframe_count = 0
        for i in range(10): # for each subframe
            if sfa[i] == SF_TYPE.D:
                start_index += 2 * N_DL_symb(dl_cp, delta_f)
            elif sfa[i] == SF_TYPE.U:
                start_index += 2 * N_UL_symb(ul_cp)
            else:
                if special_subframe_count == index:
                    start_index += symbol_nr_DwPTS(ssp, dl_cp, delta_f)
                    break
                else:
                    special_subframe_count += 1
                    start_index += symbol_nr_DwPTS(ssp, dl_cp, delta_f) + symbol_nr_GP(ssp, dl_cp, ul_cp, delta_f) + symbol_nr_UpPTS(ssp, dl_cp, ul_cp)
        logging.getLogger(__name__).debug("start_index={}, symbol_nr_GP(ssp, dl_cp, ul_cp, delta_f)={}".format(start_index, symbol_nr_GP(ssp, dl_cp, ul_cp, delta_f)))
        gp = self[start_index:start_index+symbol_nr_GP(ssp, dl_cp, ul_cp, delta_f)]
        return gp, i
    def nr_of_UpPTS(self):
        sfa = subframe_assignment(self.l1_config.subframe_assignment)
        return sfa.count(SF_TYPE.S)
    def slot_UpPTS(self, index):
        '''
        Return: slot instance, n_s
        '''
        assert 0 <= index < self.nr_of_UpPTS()
        start_index = 0
        dl_cp = self.l1_config.dl_cyclicPrefixLength
        ul_cp = self.l1_config.ul_cyclicPrefixLength
        delta_f = self.l1_config.delta_f
        ssp = self.l1_config.specialSubframePatterns
        sfa = subframe_assignment(self.l1_config.subframe_assignment)
        uppts_slot_count = 0
        for slot_index in range(20):
            if sfa[int(slot_index/2)] == SF_TYPE.D:
                start_index += N_DL_symb(dl_cp, delta_f)
            elif sfa[int(slot_index/2)] == SF_TYPE.U:
                start_index += N_UL_symb(ul_cp)
            else:   # special subframe
                if slot_index % 2 == 0:
                    start_index += N_DL_symb(dl_cp, delta_f)
                else:
                    if uppts_slot_count == index:
                        start_index += N_UL_symb(ul_cp) - symbol_nr_UpPTS(ssp, dl_cp, ul_cp)
                        break
                    else:
                        uppts_slot_count += 1
                        start_index += N_UL_symb(ul_cp)
        return self[start_index:start_index+symbol_nr_UpPTS(ssp, dl_cp, ul_cp)], slot_index
    def nr_of_DwPTS(self):
        sfa = subframe_assignment(self.l1_config.subframe_assignment)
        return sfa.count(SF_TYPE.S)
    def nr_of_DwPTS_slots(self):
        nr = self.nr_of_DwPTS()
        dl_cp = self.l1_config.dl_cyclicPrefixLength
        ssp = self.l1_config.specialSubframePatterns
        delta_f = self.l1_config.delta_f
        if symbol_nr_DwPTS(ssp, dl_cp, delta_f) > N_DL_symb(dl_cp, delta_f):
            nr *= 2
        return nr
    def slot_DwPTS(self, index):
        '''
        index: index of DwPTS in this frame. Note that one DwPTS can be split
                into two if it's longer than one slot.

        return: slot instance, n_s
        '''
        assert 0 <= index < self.nr_of_DwPTS_slots()
        start_index = 0
        dl_cp = self.l1_config.dl_cyclicPrefixLength
        ul_cp = self.l1_config.ul_cyclicPrefixLength
        delta_f = self.l1_config.delta_f
        ssp = self.l1_config.specialSubframePatterns
        sfa = subframe_assignment(self.l1_config.subframe_assignment)
        dwpts_slot_count = 0
        is_long_dwpts = symbol_nr_DwPTS(ssp, dl_cp, delta_f) > N_DL_symb(dl_cp, delta_f)
        for slot_index in range(20): # for each slot
            if sfa[int(slot_index/2)] == SF_TYPE.D:
                start_index += N_DL_symb(dl_cp, delta_f)
            elif sfa[int(slot_index/2)] == SF_TYPE.U:
                start_index += N_UL_symb(ul_cp)
            else:
                # this is a slot in special subframe
                if is_long_dwpts:
                    if slot_index % 2 == 0:  # first slot in the subframe
                        if dwpts_slot_count == index:   # this is the slot we look for
                            break
                        else:
                            dwpts_slot_count += 1
                            start_index += N_DL_symb(dl_cp, delta_f)
                    else:   # second slot in the subframe
                        if dwpts_slot_count == index:
                            break
                        else:
                            dwpts_slot_count += 1
                            start_index += symbol_nr_DwPTS(ssp, dl_cp, delta_f) + symbol_nr_GP(ssp, dl_cp, ul_cp, delta_f) + symbol_nr_UpPTS(ssp, dl_cp, ul_cp) - N_DL_symb(dl_cp, delta_f)
                else:   # DwPTS is shorter than one slot
                    if slot_index % 2 == 0:  # first slot in the special subframe, which contains DwPTS
                        if dwpts_slot_count == index:
                            break
                        else:
                            dwpts_slot_count += 1
                            start_index += N_DL_symb(dl_cp, delta_f)
                    else:
                        dwpts_slot_count += 1
                        start_index += N_UL_symb(ul_cp)
        if is_long_dwpts:
            if slot_index % 2 == 0:
                dwpts = self[start_index:start_index+N_DL_symb(dl_cp, delta_f)]
            else:
                dwpts = self[start_index:start_index+(symbol_nr_DwPTS(ssp, dl_cp, delta_f)-N_DL_symb(dl_cp, delta_f))]
        else:
            dwpts = self[start_index:start_index+symbol_nr_DwPTS(ssp, dl_cp, delta_f)]
        return dwpts, slot_index
    def __mark_GP(self):
        for index in range(self.nr_of_GP()):
            gp, n_s = self.slot_GP(index)
            X, Y = gp._sizes()
            for x in range(X):
                for y in range(Y):
                    gp[x][y] = Re(RE_TYPE.GP)
    def __mark_DwPTS(self):
        for index in range(self.nr_of_DwPTS_slots()):
            dwpts_slot, n_s = self.slot_DwPTS(index)
            X, Y = dwpts_slot._sizes()
            for x in range(X):
                for y in range(Y):
                    dwpts_slot[x][y] = Re(RE_TYPE.DWPTS)
    def __mark_UpPTS(self):
        for index in range(self.nr_of_UpPTS()):
            uppts, n_s = self.slot_UpPTS(index)
            X, Y = uppts._sizes()
            for x in range(X):
                for y in range(Y):
                    uppts[x][y] = Re(RE_TYPE.UPPTS)
    def __mark_DL(self):
        sfa = subframe_assignment(self.l1_config.subframe_assignment)
        for index in range(20):
            if sfa[int(index/2)] == SF_TYPE.D:
                dl_slot = self.slot(index)
                X, Y = dl_slot._sizes()
                for x in range(X):
                    for y in range(Y):
                        dl_slot[x][y] = Re(RE_TYPE.DL_AVAILABLE)
    def __mark_UL(self):
        sfa = subframe_assignment(self.l1_config.subframe_assignment)
        for index in range(20):
            if sfa[int(index/2)] == SF_TYPE.U:
                ul_slot = self.slot(index)
                X, Y = ul_slot._sizes()
                for x in range(X):
                    for y in range(Y):
                        ul_slot[x][y] = Re(RE_TYPE.UL_AVAILABLE)
    def __mark_CSRS(self):
        N_cell_ID = self.l1_config.PhysCellId
        bw = self.l1_config.dl_bandwidth
        sfa = subframe_assignment(self.l1_config.subframe_assignment)
        for slot_index in range(20):
            if sfa[int(slot_index/2)] == SF_TYPE.D:
                dl_slot = self.slot(slot_index)
                for p in range(ANTENNA_PORTS_COUNT.to_int(self.l1_config.antenna_ports_count)):
                    csrs_ap(dl_slot, bw, slot_index, p, N_cell_ID)
        for index in range(self.nr_of_DwPTS_slots()):
            dwpts_slot, n_s = self.slot_DwPTS(index)
            for p in range(ANTENNA_PORTS_COUNT.to_int(self.l1_config.antenna_ports_count)):
                csrs_ap(dwpts_slot, bw, n_s, p, N_cell_ID)
    def __mark_PSS(self):
        duplex_mode = self.l1_config.duplexMode
        dl_cp = self.l1_config.dl_cyclicPrefixLength
        delta_f = self.l1_config.delta_f
        N_DL_RB = BW.toRbNumber(self.l1_config.dl_bandwidth)
        N_RB_sc = BW.N_RB_sc(dl_cp, delta_f)
        n_s_list, l = pss_n_s_l(duplex_mode, N_DL_symb(dl_cp, delta_f))
        k_list = pss_k_list(N_DL_RB, N_RB_sc)
        k_reserve_list = pss_k_reserved_list(N_DL_RB, N_RB_sc)
        for n_s in n_s_list:
            slot = self.slot(n_s)
            for k in k_list:
                slot[l][k] = Re(RE_TYPE.PSS)
            for k in k_reserve_list:
                slot[l][k] = Re(RE_TYPE.RESERVED)
    def __mark_SSS(self):
        duplex_mode = self.l1_config.duplexMode
        dl_cp = self.l1_config.dl_cyclicPrefixLength
        delta_f = self.l1_config.delta_f
        N_DL_RB = BW.toRbNumber(self.l1_config.dl_bandwidth)
        N_RB_sc = BW.N_RB_sc(dl_cp, delta_f)
        n_s_list, l = sss_n_s_l(duplex_mode, N_DL_symb(dl_cp, delta_f))
        k_list = sss_k_list(N_DL_RB, N_RB_sc)
        k_reserve_list = sss_k_reserved_list(N_DL_RB, N_RB_sc)
        for n_s in n_s_list:
            slot = self.slot(n_s)
            for k in k_list:
                slot[l][k] = Re(RE_TYPE.SSS)
            for k in k_reserve_list:
                slot[l][k] = Re(RE_TYPE.RESERVED)
    def __mark_PBCH(self):
        dl_cp = self.l1_config.dl_cyclicPrefixLength
        delta_f = self.l1_config.delta_f
        bw = self.l1_config.dl_bandwidth
        N_DL_RB = BW.toRbNumber(self.l1_config.dl_bandwidth)
        N_RB_sc = BW.N_RB_sc(dl_cp, delta_f)
        N_cell_ID = self.l1_config.PhysCellId
        n_s, l_list = pbch_n_s_l()
        k_list = pbch_k_list(N_DL_RB, N_RB_sc)
        slot = self.slot(n_s)
        for l in l_list:
            for k in k_list:
                if not is_csrs_reserved(l, k, bw, n_s, N_cell_ID, N_DL_symb(dl_cp, delta_f)):
                    slot[l][k] = Re(RE_TYPE.PBCH)



    def __mark_all(self):
        self.__mark_GP()
        self.__mark_DwPTS()
        self.__mark_UpPTS()
        self.__mark_DL()
        self.__mark_UL()
        self.__mark_CSRS()
        self.__mark_PSS()
        self.__mark_SSS()
        self.__mark_PBCH()
