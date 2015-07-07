from .Matrix import Matrix
from .Enums import DUPLEX_MODE, BW, SF_TYPE, ANTENNA_PORTS_COUNT, RE_TYPE
from ..c6 import N_DL_symb, csrs
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
        slot.sf_type = sfa[int(index/2)]
        slot.n_s = index
        return slot
    def nr_of_GP(self):
        sfa = subframe_assignment(self.l1_config.subframe_assignment)
        return sfa.count(SF_TYPE.S)
    def slot_GP(self, index):
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
        return gp
    def nr_of_UpPTS(self):
        sfa = subframe_assignment(self.l1_config.subframe_assignment)
        return sfa.count(SF_TYPE.S)
    def slot_UpPTS(self, index):
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
        return self[start_index:start_index+symbol_nr_UpPTS(ssp, dl_cp, ul_cp)]
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
        return dwpts
    def __mark_GP(self):
        for index in range(self.nr_of_GP()):
            gp = self.slot_GP(index)
            X, Y = gp._sizes()
            for x in range(X):
                for y in range(Y):
                    gp[x][y] = Re(RE_TYPE.GP)
    def __mark_DwPTS(self):
        for index in range(self.nr_of_DwPTS_slots()):
            dwpts_slot = self.slot_DwPTS(index)
            X, Y = dwpts_slot._sizes()
            for x in range(X):
                for y in range(Y):
                    dwpts_slot[x][y] = Re(RE_TYPE.DWPTS)
    def __mark_UpPTS(self):
        for index in range(self.nr_of_UpPTS()):
            uppts = self.slot_UpPTS(index)
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
    def __mark_all(self):
        self.__mark_GP()
        self.__mark_DwPTS()
        self.__mark_UpPTS()
        self.__mark_DL()
        self.__mark_UL()
