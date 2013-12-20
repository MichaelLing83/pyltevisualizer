#@+leo-ver=5-thin
#@+node:Michael.20120322092817.1717: * @thin ./pyLTEVisualizer.py
#@+others
#@+node:Michael.20120322092817.2073: ** project_config
project_version = '1.0.0'
project_name = 'pyLTEVisualizer'
project_owner = "Author: Ling Duo, Email: duo.ling.cn@gmail.com"
project_weblink = "http://code.google.com/p/pyltevisualizer/"
#@+node:Michael.20120322092817.1643: ** Source codes
# RE position representation:
    # (frame, slot, l, k)
    # frame num.
    # slot num. from 0 to 19
    # l : OFDM symbol index
    # k: subcarrier index
import os
#@+others
#@+node:Michael.20120322092817.2006: *3* class Config
class Config:
    
    def __init__(self):
        #self.dir = '.'+os.sep+'Config'+os.sep
        self.config = self._get_config('config.txt')
        self.config['RA_PREAMBLE_MAPPING'] = self._get_RA_PREAMBLE_MAPPING()
        self.config['AppName'] = 'lte-phy-channel-on-air'
        self.config['version'] = '2.0'
        self.validate_config()

    #@+others
    #@+node:Michael.20120322092817.2007: *4* get_config
    def get_config(self):
        return self.config
    #@+node:Michael.20120322092817.2008: *4* validate_config
    def validate_config(self):
        '''
        Valicate configuration. This method should be called after config has been read in from the file.
        '''
        if self.config['LTE_Mode'] == 'TDD':
            # configuration validation for TDD
            if len(self.config['RA_PREAMBLE_MAPPING'][self.config['PRACH_Configuration_Index'],self.config['UL_DL_config']])==0:
                prach_config_wrong_str = '''
                PRACH resource configuration is:
                    PRACH configuration Index = %s
                    UL/DL configuration = %s
                And according to table 5.7.1-4 in 36.211 this configuration is N/A.
                '''%(self.config['PRACH_Configuration_Index'], self.config['UL_DL_config'])
                raise ConfigException(prach_config_wrong_str)
    #@+node:Michael.20120322092817.2009: *4* _get_RA_PREAMBLE_MAPPING
    def _get_RA_PREAMBLE_MAPPING(self):
        # key: (PRACH_configuration_index, UL/DL_configuration)
        # value: a tuple of preamble mapping in time and frequency
        d = dict()
        
        d[(0,0)] = ( (0,1,0,2), )
        d[(0,1)] = ( (0,1,0,1), )
        d[(0,2)] = ( (0,1,0,0), )
        d[(0,3)] = ( (0,1,0,2), )
        d[(0,4)] = ( (0,1,0,1), )
        d[(0,5)] = ( (0,1,0,0), )
        d[(0,6)] = ( (0,1,0,2), )
        
        d[(1,0)] = ( (0,2,0,2), )
        d[(1,1)] = ( (0,2,0,1), )
        d[(1,2)] = ( (0,2,0,0), )
        d[(1,3)] = ( (0,2,0,2), )
        d[(1,4)] = ( (0,2,0,1), )
        d[(1,5)] = ( (0,2,0,0), )
        d[(1,6)] = ( (0,2,0,2), )
        
        d[(2,0)] = ( (0,1,1,2), )
        d[(2,1)] = ( (0,1,1,1), )
        d[(2,2)] = ( (0,1,1,0), )
        d[(2,3)] = ( (0,1,0,1), )
        d[(2,4)] = ( (0,1,0,0), )
        d[(2,5)] = (  )
        d[(2,6)] = ( (0,1,1,1), )
        
        d[(3,0)] = ( (0,0,0,2), )
        d[(3,1)] = ( (0,0,0,1), )
        d[(3,2)] = ( (0,0,0,0), )
        d[(3,3)] = ( (0,0,0,2), )
        d[(3,4)] = ( (0,0,0,1), )
        d[(3,5)] = ( (0,0,0,0), )
        d[(3,6)] = ( (0,0,0,2), )
        
        d[(4,0)] = ( (0,0,1,2), )
        d[(4,1)] = ( (0,0,1,1), )
        d[(4,2)] = ( (0,0,1,0), )
        d[(4,3)] = ( (0,0,0,1), )
        d[(4,4)] = ( (0,0,0,0), )
        d[(4,5)] = (  )
        d[(4,6)] = ( (0,0,1,1), )
        
        d[(5,0)] = ( (0,0,0,1), )
        d[(5,1)] = ( (0,0,0,0), )
        d[(5,2)] = (  )
        d[(5,3)] = ( (0,0,0,0), )
        d[(5,4)] = (  )
        d[(5,5)] = (  )
        d[(5,6)] = ( (0,0,0,1), )
        
        d[(6,0)] = ( (0,0,0,2),(0,0,1,2) )
        d[(6,1)] = ( (0,0,0,1),(0,0,1,1) )
        d[(6,2)] = ( (0,0,0,0),(0,0,1,0) )
        d[(6,3)] = ( (0,0,0,1),(0,0,0,2) )
        d[(6,4)] = ( (0,0,0,0),(0,0,0,1) )
        d[(6,5)] = ( (0,0,0,0),(1,0,0,0) )
        d[(6,6)] = ( (0,0,0,2),(0,0,1,1) )
        
        d[(7,0)] = ( (0,0,0,1),(0,0,1,1) )
        d[(7,1)] = ( (0,0,0,0),(0,0,1,0) )
        d[(7,2)] = (  )
        d[(7,3)] = ( (0,0,0,0),(0,0,0,2) )
        d[(7,4)] = (  )
        d[(7,5)] = (  )
        d[(7,6)] = ( (0,0,0,1),(0,0,1,0) )
        
        d[(8,0)] = ( (0,0,0,0),(0,0,1,0) )
        d[(8,1)] = (  )
        d[(8,2)] = (  )
        d[(8,3)] = ( (0,0,0,0),(0,0,0,1) )
        d[(8,4)] = (  )
        d[(8,5)] = (  )
        d[(8,6)] = ( (0,0,0,0),(0,0,1,1) )
        
        d[(9,0)] = ( (0,0,0,1),(0,0,0,2),(0,0,1,2) )
        d[(9,1)] = ( (0,0,0,0),(0,0,0,1),(0,0,1,1) )
        d[(9,2)] = ( (0,0,0,0),(0,0,1,0),(1,0,0,0) )
        d[(9,3)] = ( (0,0,0,0),(0,0,0,1),(0,0,0,2) )
        d[(9,4)] = ( (0,0,0,0),(0,0,0,1),(1,0,0,1) )
        d[(9,5)] = ( (0,0,0,0),(1,0,0,0),(2,0,0,0) )
        d[(9,6)] = ( (0,0,0,1),(0,0,0,2),(0,0,1,1) )
        
        d[(10,0)] = ( (0,0,0,0),(0,0,1,0),(0,0,1,1) )
        d[(10,1)] = ( (0,0,0,1),(0,0,1,0),(0,0,1,1) )
        d[(10,2)] = ( (0,0,0,0),(0,0,1,0),(1,0,1,0) )
        d[(10,3)] = (  )
        d[(10,4)] = ( (0,0,0,0),(0,0,0,1),(1,0,0,0) )
        d[(10,5)] = (  )
        d[(10,6)] = ( (0,0,0,0),(0,0,0,2),(0,0,1,0) )
        
        
        d[(11,0)] = (  )
        d[(11,1)] = ( (0,0,0,0),(0,0,0,1),(0,0,1,0) )
        d[(11,2)] = (  )
        d[(11,3)] = (  )
        d[(11,4)] = (  )
        d[(11,5)] = (  )
        d[(11,6)] = ( (0,0,0,1),(0,0,1,0),(0,0,1,1) )
        
        d[(12,0)] = ( (0,0,0,1),(0,0,0,2),(0,0,1,1),(0,0,1,2) )
        d[(12,1)] = ( (0,0,0,0),(0,0,0,1),(0,0,1,0),(0,0,1,1) )
        d[(12,2)] = ( (0,0,0,0),(0,0,1,0),(1,0,0,0),(1,0,1,0) )
        d[(12,3)] = ( (0,0,0,0),(0,0,0,1),(0,0,0,2),(1,0,0,2) )
        d[(12,4)] = ( (0,0,0,0),(0,0,0,1),(1,0,0,0),(1,0,0,1) )
        d[(12,5)] = ( (0,0,0,0),(1,0,0,0),(2,0,0,0),(3,0,0,0) )
        d[(12,6)] = ( (0,0,0,1),(0,0,0,2),(0,0,1,0),(0,0,1,1) )
        
        d[(13,0)] = ( (0,0,0,0),(0,0,0,2),(0,0,1,0),(0,0,1,2) )
        d[(13,1)] = (  )
        d[(13,2)] = (  )
        d[(13,3)] = ( (0,0,0,0),(0,0,0,1),(0,0,0,2),(1,0,0,1) )
        d[(13,4)] = (  )
        d[(13,5)] = (  )
        d[(13,6)] = ( (0,0,0,0),(0,0,0,1),(0,0,0,2),(0,0,1,1) )
        
        d[(14,0)] = ( (0,0,0,0),(0,0,0,1),(0,0,1,0),(0,0,1,1) )
        d[(14,1)] = (  )
        d[(14,2)] = (  )
        d[(14,3)] = ( (0,0,0,0),(0,0,0,1),(0,0,0,2),(1,0,0,0) )
        d[(14,4)] = (  )
        d[(14,5)] = (  )
        d[(14,6)] = ( (0,0,0,0),(0,0,0,2),(0,0,1,0),(0,0,1,1) )
        
        d[(15,0)] = ( (0,0,0,0),(0,0,0,1),(0,0,0,2),(0,0,1,1),(0,0,1,2) )
        d[(15,1)] = ( (0,0,0,0),(0,0,0,1),(0,0,1,0),(0,0,1,1),(1,0,0,1) )
        d[(15,2)] = ( (0,0,0,0),(0,0,1,0),(1,0,0,0),(1,0,1,0),(2,0,0,0) )
        d[(15,3)] = ( (0,0,0,0),(0,0,0,1),(0,0,0,2),(1,0,0,1),(1,0,0,2) )
        d[(15,4)] = ( (0,0,0,0),(0,0,0,1),(1,0,0,0),(1,0,0,1),(2,0,0,1) )
        d[(15,5)] = ( (0,0,0,0),(1,0,0,0),(2,0,0,0),(3,0,0,0),(4,0,0,0) )
        d[(15,6)] = ( (0,0,0,0),(0,0,0,1),(0,0,0,2),(0,0,1,0),(0,0,1,1) )
        
        d[(16,0)] = ( (0,0,0,1),(0,0,0,2),(0,0,1,0),(0,0,1,1),(0,0,1,2) )
        d[(16,1)] = ( (0,0,0,0),(0,0,0,1),(0,0,1,0),(0,0,1,1),(1,0,1,1) )
        d[(16,2)] = ( (0,0,0,0),(0,0,1,0),(1,0,0,0),(1,0,1,0),(2,0,1,0) )
        d[(16,3)] = ( (0,0,0,0),(0,0,0,1),(0,0,0,2),(1,0,0,0),(1,0,0,2) )
        d[(16,4)] = ( (0,0,0,0),(0,0,0,1),(1,0,0,0),(1,0,0,1),(2,0,0,0) )
        d[(16,5)] = (  )
        d[(16,6)] = (  )
        
        d[(17,0)] = ( (0,0,0,0),(0,0,0,1),(0,0,0,2),(0,0,1,0),(0,0,1,2) )
        d[(17,1)] = ( (0,0,0,0),(0,0,0,1),(0,0,1,0),(0,0,1,1),(1,0,0,0) )
        d[(17,2)] = (  )
        d[(17,3)] = ( (0,0,0,0),(0,0,0,1),(0,0,0,2),(1,0,0,0),(1,0,0,1) )
        d[(17,4)] = (  )
        d[(17,5)] = (  )
        d[(17,6)] = (  )
        
        d[(18,0)] = ( (0,0,0,0),(0,0,0,1),(0,0,0,2),(0,0,1,0),(0,0,1,1),(0,0,1,2) )
        d[(18,1)] = ( (0,0,0,0),(0,0,0,1),(0,0,1,0),(0,0,1,1),(1,0,0,1),(1,0,1,1) )
        d[(18,2)] = ( (0,0,0,0),(0,0,1,0),(1,0,0,0),(1,0,1,0),(2,0,0,0),(2,0,1,0) )
        d[(18,3)] = ( (0,0,0,0),(0,0,0,1),(0,0,0,2),(1,0,0,0),(1,0,0,1),(1,0,0,2) )
        d[(18,4)] = ( (0,0,0,0),(0,0,0,1),(1,0,0,0),(1,0,0,1),(2,0,0,0),(2,0,0,1) )
        d[(18,5)] = ( (0,0,0,0),(1,0,0,0),(2,0,0,0),(3,0,0,0),(4,0,0,0),(5,0,0,0) )
        d[(18,6)] = ( (0,0,0,0),(0,0,0,1),(0,0,0,2),(0,0,1,0),(0,0,1,1),(1,0,0,2) )
        
        d[(19,0)] = (  )
        d[(19,1)] = ( (0,0,0,0),(0,0,0,1),(0,0,1,0),(0,0,1,1),(1,0,0,0),(1,0,1,0) )
        d[(19,2)] = (  )
        d[(19,3)] = (  )
        d[(19,4)] = (  )
        d[(19,5)] = (  )
        d[(19,6)] = ( (0,0,0,0),(0,0,0,1),(0,0,0,2),(0,0,1,0),(0,0,1,1),(1,0,1,1) )
        
        d[(20,0)] = ( (0,1,0,1), )
        d[(20,1)] = ( (0,1,0,0), )
        d[(20,2)] = (  )
        d[(20,3)] = ( (0,1,0,1), )
        d[(20,4)] = ( (0,1,0,0), )
        d[(20,5)] = (  )
        d[(20,6)] = ( (0,1,0,1), )
        d[(30,0)] = d[(20,0)]
        d[(30,1)] = d[(20,1)]
        d[(30,2)] = d[(20,2)]
        d[(30,3)] = d[(20,3)]
        d[(30,4)] = d[(20,4)]
        d[(30,5)] = d[(20,5)]
        d[(30,6)] = d[(20,6)]
        
        d[(21,0)] = ( (0,2,0,1), )
        d[(21,1)] = ( (0,2,0,0), )
        d[(21,2)] = (  )
        d[(21,3)] = ( (0,2,0,1), )
        d[(21,4)] = ( (0,2,0,0), )
        d[(21,5)] = (  )
        d[(21,6)] = ( (0,2,0,1), )
        d[(31,0)] = d[(21,0)]
        d[(31,1)] = d[(21,1)]
        d[(31,2)] = d[(21,2)]
        d[(31,3)] = d[(21,3)]
        d[(31,4)] = d[(21,4)]
        d[(31,5)] = d[(21,5)]
        d[(31,6)] = d[(21,6)]
        
        d[(22,0)] = ( (0,1,1,1), )
        d[(22,1)] = ( (0,1,1,0), )
        d[(22,2)] = (  )
        d[(22,3)] = (  )
        d[(22,4)] = (  )
        d[(22,5)] = (  )
        d[(22,6)] = ( (0,1,1,0), )
        d[(32,0)] = d[(22,0)]
        d[(32,1)] = d[(22,1)]
        d[(32,2)] = d[(22,2)]
        d[(32,3)] = d[(22,3)]
        d[(32,4)] = d[(22,4)]
        d[(32,5)] = d[(22,5)]
        d[(32,6)] = d[(22,6)]
        
        d[(23,0)] = ( (0,0,0,1), )
        d[(23,1)] = ( (0,0,0,0), )
        d[(23,2)] = (  )
        d[(23,3)] = ( (0,0,0,1), )
        d[(23,4)] = ( (0,0,0,0), )
        d[(23,5)] = (  )
        d[(23,6)] = ( (0,0,0,1), )
        d[(33,0)] = d[(23,0)]
        d[(33,1)] = d[(23,1)]
        d[(33,2)] = d[(23,2)]
        d[(33,3)] = d[(23,3)]
        d[(33,4)] = d[(23,4)]
        d[(33,5)] = d[(23,5)]
        d[(33,6)] = d[(23,6)]
        
        d[(24,0)] = ( (0,0,1,1), )
        d[(24,1)] = ( (0,0,1,0), )
        d[(24,2)] = (  )
        d[(24,3)] = (  )
        d[(24,4)] = (  )
        d[(24,5)] = (  )
        d[(24,6)] = ( (0,0,1,0), )
        d[(34,0)] = d[(24,0)]
        d[(34,1)] = d[(24,1)]
        d[(34,2)] = d[(24,2)]
        d[(34,3)] = d[(24,3)]
        d[(34,4)] = d[(24,4)]
        d[(34,5)] = d[(24,5)]
        d[(34,6)] = d[(24,6)]
        
        d[(25,0)] = ( (0,0,0,1),(0,0,1,1) )
        d[(25,1)] = ( (0,0,0,0),(0,0,1,0) )
        d[(25,2)] = (  )
        d[(25,3)] = ( (0,0,0,1),(1,0,0,1) )
        d[(25,4)] = ( (0,0,0,0),(1,0,0,0) )
        d[(25,5)] = (  )
        d[(25,6)] = ( (0,0,0,1),(0,0,1,0) )
        d[(35,0)] = d[(25,0)]
        d[(35,1)] = d[(25,1)]
        d[(35,2)] = d[(25,2)]
        d[(35,3)] = d[(25,3)]
        d[(35,4)] = d[(25,4)]
        d[(35,5)] = d[(25,5)]
        d[(35,6)] = d[(25,6)]
        
        d[(26,0)] = ( (0,0,0,1),(0,0,1,1),(1,0,0,1) )
        d[(26,1)] = ( (0,0,0,0),(0,0,1,0),(1,0,0,0) )
        d[(26,2)] = (  )
        d[(26,3)] = ( (0,0,0,1),(1,0,0,1),(2,0,0,1) )
        d[(26,4)] = ( (0,0,0,0),(1,0,0,0),(2,0,0,0) )
        d[(26,5)] = (  )
        d[(26,6)] = ( (0,0,0,1),(0,0,1,0),(1,0,0,1) )
        d[(36,0)] = d[(26,0)]
        d[(36,1)] = d[(26,1)]
        d[(36,2)] = d[(26,2)]
        d[(36,3)] = d[(26,3)]
        d[(36,4)] = d[(26,4)]
        d[(36,5)] = d[(26,5)]
        d[(36,6)] = d[(26,6)]
        
        d[(27,0)] = ( (0,0,0,1),(0,0,1,1),(1,0,0,1),(1,0,1,1) )
        d[(27,1)] = ( (0,0,0,0),(0,0,1,0),(1,0,0,0),(1,0,1,0) )
        d[(27,2)] = (  )
        d[(27,3)] = ( (0,0,0,1),(1,0,0,1),(2,0,0,1),(3,0,0,1) )
        d[(27,4)] = ( (0,0,0,0),(1,0,0,0),(2,0,0,0),(3,0,0,0) )
        d[(27,5)] = (  )
        d[(27,6)] = ( (0,0,0,1),(0,0,1,0),(1,0,0,1),(1,0,1,0) )
        d[(37,0)] = d[(27,0)]
        d[(37,1)] = d[(27,1)]
        d[(37,2)] = d[(27,2)]
        d[(37,3)] = d[(27,3)]
        d[(37,4)] = d[(27,4)]
        d[(37,5)] = d[(27,5)]
        d[(37,6)] = d[(27,6)]
        
        d[(28,0)] = ( (0,0,0,1),(0,0,1,1),(1,0,0,1),(1,0,1,1),(2,0,0,1) )
        d[(28,1)] = ( (0,0,0,0),(0,0,1,0),(1,0,0,0),(1,0,1,0),(2,0,0,0) )
        d[(28,2)] = (  )
        d[(28,3)] = ( (0,0,0,1),(1,0,0,1),(2,0,0,1),(3,0,0,1),(4,0,0,1) )
        d[(28,4)] = ( (0,0,0,0),(1,0,0,0),(2,0,0,0),(3,0,0,0),(4,0,0,0) )
        d[(28,5)] = (  )
        d[(28,6)] = ( (0,0,0,1),(0,0,1,0),(1,0,0,1),(1,0,1,0),(2,0,0,1) )
        d[(38,0)] = d[(28,0)]
        d[(38,1)] = d[(28,1)]
        d[(38,2)] = d[(28,2)]
        d[(38,3)] = d[(28,3)]
        d[(38,4)] = d[(28,4)]
        d[(38,5)] = d[(28,5)]
        d[(38,6)] = d[(28,6)]
        
        d[(29,0)] = ( (0,0,0,1),(0,0,1,1),(1,0,0,1),(1,0,1,1),(2,0,0,1),(2,0,1,1) )
        d[(29,1)] = ( (0,0,0,0),(0,0,1,0),(1,0,0,0),(1,0,1,0),(2,0,0,0),(2,0,1,0) )
        d[(29,2)] = (  )
        d[(29,3)] = ( (0,0,0,1),(1,0,0,1),(2,0,0,1),(3,0,0,1),(4,0,0,1),(5,0,0,1) )
        d[(29,4)] = ( (0,0,0,0),(1,0,0,0),(2,0,0,0),(3,0,0,0),(4,0,0,0),(5,0,0,0) )
        d[(29,5)] = (  )
        d[(29,6)] = ( (0,0,0,1),(0,0,1,0),(1,0,0,1),(1,0,1,0),(2,0,0,1),(2,0,1,0) )
        d[(39,0)] = d[(29,0)]
        d[(39,1)] = d[(29,1)]
        d[(39,2)] = d[(29,2)]
        d[(39,3)] = d[(29,3)]
        d[(39,4)] = d[(29,4)]
        d[(39,5)] = d[(29,5)]
        d[(39,6)] = d[(29,6)]
        
        d[(40,0)] = ( (0,1,0,0), )
        d[(40,1)] = (  )
        d[(40,2)] = (  )
        d[(40,3)] = ( (0,1,0,0), )
        d[(40,4)] = (  )
        d[(40,5)] = (  )
        d[(40,6)] = ( (0,1,0,0), )
        
        d[(41,0)] = ( (0,2,0,0), )
        d[(41,1)] = (  )
        d[(41,2)] = (  )
        d[(41,3)] = ( (0,2,0,0), )
        d[(41,4)] = (  )
        d[(41,5)] = (  )
        d[(41,6)] = ( (0,2,0,0), )
        
        d[(42,0)] = ( (0,1,1,0), )
        d[(42,1)] = (  )
        d[(42,2)] = (  )
        d[(42,3)] = (  )
        d[(42,4)] = (  )
        d[(42,5)] = (  )
        d[(42,6)] = (  )
        
        d[(43,0)] = ( (0,0,0,0), )
        d[(43,1)] = (  )
        d[(43,2)] = (  )
        d[(43,3)] = ( (0,0,0,0), )
        d[(43,4)] = (  )
        d[(43,5)] = (  )
        d[(43,6)] = ( (0,0,0,0), )
        
        d[(44,0)] = ( (0,0,1,0), )
        d[(44,1)] = (  )
        d[(44,2)] = (  )
        d[(44,3)] = (  )
        d[(44,4)] = (  )
        d[(44,5)] = (  )
        d[(44,6)] = (  )
        
        d[(45,0)] = ( (0,0,0,0),(0,0,1,0) )
        d[(45,1)] = (  )
        d[(45,2)] = (  )
        d[(45,3)] = ( (0,0,0,0),(1,0,0,0) )
        d[(45,4)] = (  )
        d[(45,5)] = (  )
        d[(45,6)] = ( (0,0,0,0),(1,0,0,0) )
        
        d[(46,0)] = ( (0,0,0,0),(0,0,1,0),(1,0,0,0) )
        d[(46,1)] = (  )
        d[(46,2)] = (  )
        d[(46,3)] = ( (0,0,0,0),(1,0,0,0),(2,0,0,0) )
        d[(46,4)] = (  )
        d[(46,5)] = (  )
        d[(46,6)] = ( (0,0,0,0),(1,0,0,0),(2,0,0,0) )
        
        d[(47,0)] = ( (0,0,0,0),(0,0,1,0),(1,0,0,0),(1,0,1,0) )
        d[(47,1)] = (  )
        d[(47,2)] = (  )
        d[(47,3)] = ( (0,0,0,0),(1,0,0,0),(2,0,0,0),(3,0,0,0) )
        d[(47,4)] = (  )
        d[(47,5)] = (  )
        d[(47,6)] = ( (0,0,0,0),(1,0,0,0),(2,0,0,0),(3,0,0,0) )
        
        d[(48,0)] = ( (0,1,0,-1), )
        d[(48,1)] = ( (0,1,0,-1), )
        d[(48,2)] = ( (0,1,0,-1), )
        d[(48,3)] = ( (0,1,0,-1), )
        d[(48,4)] = ( (0,1,0,-1), )
        d[(48,5)] = ( (0,1,0,-1), )
        d[(48,6)] = ( (0,1,0,-1), )
        
        d[(49,0)] = ( (0,2,0,-1), )
        d[(49,1)] = ( (0,2,0,-1), )
        d[(49,2)] = ( (0,2,0,-1), )
        d[(49,3)] = ( (0,2,0,-1), )
        d[(49,4)] = ( (0,2,0,-1), )
        d[(49,5)] = ( (0,2,0,-1), )
        d[(49,6)] = ( (0,2,0,-1), )
        
        d[(50,0)] = ( (0,1,1,-1), )
        d[(50,1)] = ( (0,1,1,-1), )
        d[(50,2)] = ( (0,1,1,-1), )
        d[(50,3)] = (  )
        d[(50,4)] = (  )
        d[(50,5)] = (  )
        d[(50,6)] = ( (0,1,1,-1), )
        
        d[(51,0)] = ( (0,0,0,-1), )
        d[(51,1)] = ( (0,0,0,-1), )
        d[(51,2)] = ( (0,0,0,-1), )
        d[(51,3)] = ( (0,0,0,-1), )
        d[(51,4)] = ( (0,0,0,-1), )
        d[(51,5)] = ( (0,0,0,-1), )
        d[(51,6)] = ( (0,0,0,-1), )
        
        d[(52,0)] = ( (0,0,1,-1), )
        d[(52,1)] = ( (0,0,1,-1), )
        d[(52,2)] = ( (0,0,1,-1), )
        d[(52,3)] = (  )
        d[(52,4)] = (  )
        d[(52,5)] = (  )
        d[(52,6)] = ( (0,0,1,-1), )
        
        d[(53,0)] = ( (0,0,0,-1),(0,0,1,-1) )
        d[(53,1)] = ( (0,0,0,-1),(0,0,1,-1) )
        d[(53,2)] = ( (0,0,0,-1),(0,0,1,-1) )
        d[(53,3)] = ( (0,0,0,-1),(1,0,0,-1) )
        d[(53,4)] = ( (0,0,0,-1),(1,0,0,-1) )
        d[(53,5)] = ( (0,0,0,-1),(1,0,0,-1) )
        d[(53,6)] = ( (0,0,0,-1),(0,0,1,-1) )
        
        d[(54,0)] = ( (0,0,0,-1),(0,0,1,-1),(1,0,0,-1) )
        d[(54,1)] = ( (0,0,0,-1),(0,0,1,-1),(1,0,0,-1) )
        d[(54,2)] = ( (0,0,0,-1),(0,0,1,-1),(1,0,0,-1) )
        d[(54,3)] = ( (0,0,0,-1),(1,0,0,-1),(2,0,0,-1) )
        d[(54,4)] = ( (0,0,0,-1),(1,0,0,-1),(2,0,0,-1) )
        d[(54,5)] = ( (0,0,0,-1),(1,0,0,-1),(2,0,0,-1) )
        d[(54,6)] = ( (0,0,0,-1),(0,0,1,-1),(1,0,0,-1) )
        
        d[(55,0)] = ( (0,0,0,-1),(0,0,1,-1),(1,0,0,-1),(1,0,1,-1) )
        d[(55,1)] = ( (0,0,0,-1),(0,0,1,-1),(1,0,0,-1),(1,0,1,-1) )
        d[(55,2)] = ( (0,0,0,-1),(0,0,1,-1),(1,0,0,-1),(1,0,1,-1) )
        d[(55,3)] = ( (0,0,0,-1),(1,0,0,-1),(2,0,0,-1),(3,0,0,-1) )
        d[(55,4)] = ( (0,0,0,-1),(1,0,0,-1),(2,0,0,-1),(3,0,0,-1) )
        d[(55,5)] = ( (0,0,0,-1),(1,0,0,-1),(2,0,0,-1),(3,0,0,-1) )
        d[(55,6)] = ( (0,0,0,-1),(0,0,1,-1),(1,0,0,-1),(1,0,1,-1) )
        
        d[(56,0)] = ( (0,0,0,-1),(0,0,1,-1),(1,0,0,-1),(1,0,1,-1),(2,0,0,-1) )
        d[(56,1)] = ( (0,0,0,-1),(0,0,1,-1),(1,0,0,-1),(1,0,1,-1),(2,0,0,-1) )
        d[(56,2)] = ( (0,0,0,-1),(0,0,1,-1),(1,0,0,-1),(1,0,1,-1),(2,0,0,-1) )
        d[(56,3)] = ( (0,0,0,-1),(1,0,0,-1),(2,0,0,-1),(3,0,0,-1),(4,0,0,-1) )
        d[(56,4)] = ( (0,0,0,-1),(1,0,0,-1),(2,0,0,-1),(3,0,0,-1),(4,0,0,-1) )
        d[(56,5)] = ( (0,0,0,-1),(1,0,0,-1),(2,0,0,-1),(3,0,0,-1),(4,0,0,-1) )
        d[(56,6)] = ( (0,0,0,-1),(0,0,1,-1),(1,0,0,-1),(1,0,1,-1),(2,0,0,-1) )
        
        d[(57,0)] = ( (0,0,0,-1),(0,0,1,-1),(1,0,0,-1),(1,0,1,-1),(2,0,0,-1),(2,0,1,-1) )
        d[(57,1)] = ( (0,0,0,-1),(0,0,1,-1),(1,0,0,-1),(1,0,1,-1),(2,0,0,-1),(2,0,1,-1) )
        d[(57,2)] = ( (0,0,0,-1),(0,0,1,-1),(1,0,0,-1),(1,0,1,-1),(2,0,0,-1),(2,0,1,-1) )
        d[(57,3)] = ( (0,0,0,-1),(1,0,0,-1),(2,0,0,-1),(3,0,0,-1),(4,0,0,-1),(5,0,0,-1) )
        d[(57,4)] = ( (0,0,0,-1),(1,0,0,-1),(2,0,0,-1),(3,0,0,-1),(4,0,0,-1),(5,0,0,-1) )
        d[(57,5)] = ( (0,0,0,-1),(1,0,0,-1),(2,0,0,-1),(3,0,0,-1),(4,0,0,-1),(5,0,0,-1) )
        d[(57,6)] = ( (0,0,0,-1),(0,0,1,-1),(1,0,0,-1),(1,0,1,-1),(2,0,0,-1),(2,0,1,-1) )
        
        d[(58,0)] = (  )
        d[(58,1)] = (  )
        d[(58,2)] = (  )
        d[(58,3)] = (  )
        d[(58,4)] = (  )
        d[(58,5)] = (  )
        d[(58,6)] = (  )
        
        d[(59,0)] = (  )
        d[(59,1)] = (  )
        d[(59,2)] = (  )
        d[(59,3)] = (  )
        d[(59,4)] = (  )
        d[(59,5)] = (  )
        d[(59,6)] = (  )
        
        d[(60,0)] = (  )
        d[(60,1)] = (  )
        d[(60,2)] = (  )
        d[(60,3)] = (  )
        d[(60,4)] = (  )
        d[(60,5)] = (  )
        d[(60,6)] = (  )
        
        d[(61,0)] = (  )
        d[(61,1)] = (  )
        d[(61,2)] = (  )
        d[(61,3)] = (  )
        d[(61,4)] = (  )
        d[(61,5)] = (  )
        d[(61,6)] = (  )
        
        d[(62,0)] = (  )
        d[(62,1)] = (  )
        d[(62,2)] = (  )
        d[(62,3)] = (  )
        d[(62,4)] = (  )
        d[(62,5)] = (  )
        d[(62,6)] = (  )
        
        d[(63,0)] = (  )
        d[(63,1)] = (  )
        d[(63,2)] = (  )
        d[(63,3)] = (  )
        d[(63,4)] = (  )
        d[(63,5)] = (  )
        d[(63,6)] = (  )
        
        return d
    #@+node:Michael.20120322092817.2010: *4* _get_base_config
    def _get_base_config(self, filename):
        file = open(filename, 'r')
        config = dict()
    #    print 111
        for line in file:
    #        print line
            if len(line) >5 and line[0] != '#' and line[0] != ' ':
                line = line.split()
                config[line[0]] = int(float(line[1]))
        file.close()
        return config
    #@+node:Michael.20120322092817.2011: *4* _get_config
    def _get_config(self, filename):
        #filename = self.dir + filename
        config = self._get_base_config(filename)
        
        if config['LTE_Mode'] == 0:
            config['LTE_Mode'] = 'FDD'
        elif config['LTE_Mode'] == 1:
            config['LTE_Mode'] = 'TDD'

        config['draw_offset'] = Point(config['draw_offset_x'],config['draw_offset_y'])

        if config['CP_DL_type'] == 0:  #normal CP for DL
            config['N_DL_symb'] = 7
        else:
            config['N_DL_symb'] = 6

        if config['CP_UL_type'] == 0:  #normal CP for UL
            config['N_UL_symb'] = 7
        else:
            config['N_UL_symb'] = 6

        # according to table 5.6-1 in 36.101
        if config['sys_BW'] == 1:
            # because of current restriction of _get_base_config, 1.4 will become integer 1
            config['N_DL_RB'] = 6
            config['N_UL_RB'] = 6
        elif config['sys_BW'] == 3:
            config['N_DL_RB'] = 15
            config['N_UL_RB'] = 15
        elif config['sys_BW'] == 5:
            config['N_DL_RB'] = 25
            config['N_UL_RB'] = 25
        elif config['sys_BW'] == 10:
            config['N_DL_RB'] = 50
            config['N_UL_RB'] = 50
        elif config['sys_BW'] == 15:
            config['N_DL_RB'] = 75
            config['N_UL_RB'] = 75
        elif config['sys_BW'] == 20:
            config['N_DL_RB'] = 100
            config['N_UL_RB'] = 100

        #DL&UL config
        if config['UL_DL_config'] == 0:
            config['UL_DL_S'] = 'DSUUUDSUUU'
        elif config['UL_DL_config'] == 1:
            config['UL_DL_S'] = 'DSUUDDSUUD'
        elif config['UL_DL_config'] == 2:
            config['UL_DL_S'] = 'DSUDDDSUDD'
        elif config['UL_DL_config'] == 3:
            config['UL_DL_S'] = 'DSUUUDDDDD'
        elif config['UL_DL_config'] == 4:
            config['UL_DL_S'] = 'DSUUDDDDDD'
        elif config['UL_DL_config'] == 5:
            config['UL_DL_S'] = 'DSUDDDDDDD'
        elif config['UL_DL_config'] == 6:
            config['UL_DL_S'] = 'DSUUUDSUUD'

        # cell ID
        config['N_cell_ID'] = 3*config['N_cell_ID_1'] + config['N_cell_ID_2']

        # special subframe
        # calculate how many symbols are there in the DwPTS part of a special subframe
        if config['CP_DL_type'] == 0:
            if config['special_subframe_config'] in (0,5):
                config['DwPTS'] = 3
            elif config['special_subframe_config'] in (1,6):
                config['DwPTS'] = 9
            elif config['special_subframe_config'] in (7,2):
                config['DwPTS'] = 10
            elif config['special_subframe_config'] in (8,3):
                config['DwPTS'] = 11
            elif config['special_subframe_config'] == 4:
                config['DwPTS'] = 12
        else:
            if config['special_subframe_config'] in (0,4):
                config['DwPTS'] = 3
            elif config['special_subframe_config'] in (1,5):
                config['DwPTS'] = 8
            elif config['special_subframe_config'] in (2,6):
                config['DwPTS'] = 9
            elif config['special_subframe_config'] == 3:
                config['DwPTS'] = 10
            
        # calculate how many symbols are there in the UpPTS part of a special subframe
        if config['CP_DL_type'] == 0:
            if config['special_subframe_config'] in (0,1,2,3,4):
                config['UpPTS'] = 1
            elif config['special_subframe_config'] in (5,6,7,8):
                config['UpPTS'] = 2
        else:   # Extended CP
            if config['special_subframe_config'] in (0,1,2,3):
                config['UpPTS'] = 1
            elif config['special_subframe_config'] in (4,5,6):
                config['DwPTS'] = 2

        return config

    #@-others
#@+node:Michael.20120322092817.1929: *3* class ImageDrawer
from copy import deepcopy
import md5
from time import time
import Image, ImageDraw

class ImageDrawer:
    def __init__(self, config, re_lattice, re_size_lattice):
        self.config = config
        self.re_lattice = re_lattice
        self.re_size_lattice = re_size_lattice
        self.initialize_drawer()
        self.RB_count = 0
        self.draw('%s.png'%project_name)
    
    #@+others
    #@+node:Michael.20120322092817.1932: *4* _draw_lattice
    def _draw_lattice(self):
        # initialize pen colors
        penclr_D = ( self.config['color_line_DL_RE_r'], self.config['color_line_DL_RE_g'], self.config['color_line_DL_RE_b'], self.config['color_line_DL_RE_alpha'] )
        penclr_U = ( self.config['color_line_UL_RE_r'], self.config['color_line_UL_RE_g'], self.config['color_line_UL_RE_b'], self.config['color_line_UL_RE_alpha'] )
        penclr_S = ( self.config['color_line_S_RE_r'], self.config['color_line_S_RE_g'], self.config['color_line_S_RE_b'], self.config['color_line_S_RE_alpha'] )
        
        # draw all vertical lines
        start_pos = Point( 0,0 ) + self.config['draw_offset']
        total_width = 0
        total_height = self.config['cell_height']*self.config['N_DL_RB']*12
        for frame in range(self.config['start_SFN'],self.config['start_SFN']+self.config['frame_num']):
            for subframe in range(10):
                if self.config['UL_DL_S'][subframe] == 'D':
                    penclr = penclr_D
                elif self.config['UL_DL_S'][subframe] == 'U':
                    penclr = penclr_U
                else:
                    penclr = penclr_S
                if frame==self.config['start_SFN'] and subframe==0:  # this is not the starting subframe of the first frame
                    pass
                else:
                    start_pos += Point(1,0)
                    total_width += 1
                subframe_start_pos = start_pos
                subframe_width = 0
                line = (start_pos.x,start_pos.y, start_pos.x,start_pos.y+total_height)
                self.dc.line( line, penclr )
                # draw vertical lines
                for l in range(14):
                    if self.re_size_lattice.has_key( (frame,subframe,l,0) ):
                        current_symbol_length = round(self.re_size_lattice[(frame,subframe,l,0)][0]/(2048+144.)*self.config['cell_width'])
                        total_width += current_symbol_length
                        subframe_width += current_symbol_length
                        line = (start_pos.x+current_symbol_length,start_pos.y, start_pos.x+current_symbol_length,start_pos.y+total_height)
                        start_pos += Point(current_symbol_length,0)
                        self.dc.line( line, penclr )
                
                # draw horizontal lines for this subframe
                if self.config['UL_DL_S'][subframe] in 'DU':
                    for k in range(self.config['N_DL_RB']*12+1):
                        line = (subframe_start_pos.x,subframe_start_pos.y, subframe_start_pos.x+subframe_width,subframe_start_pos.y)
                        subframe_start_pos += Point(0,self.config['cell_height'])
                        self.dc.line( line, penclr )
                else:   # S
                    for k in range(self.config['N_DL_RB']*12+1):
                        line = (subframe_start_pos.x,subframe_start_pos.y, subframe_start_pos.x+self.re_size_lattice.DwPTS_width,subframe_start_pos.y)
                        self.dc.line( line, penclr )
                        line = (subframe_start_pos.x+self.re_size_lattice.DwPTS_width+self.re_size_lattice.GAP_width,subframe_start_pos.y, subframe_start_pos.x+subframe_width,subframe_start_pos.y)
                        self.dc.line( line, penclr )
                        subframe_start_pos += Point(0,self.config['cell_height'])
            start_pos += Point(self.config['frame_interval'], 0)
    #@+node:Michael.20120322092817.1935: *4* _draw_legend
    def _draw_legend(self):
        
        font = self.dc.getfont()
        legend_config = list()
        channel_list = ('CSRS_AP0','CSRS_AP1','CSRS_AP2','CSRS_AP3','PBCH','PSS','SSS','PCFICH','PHICH','PDCCH','PRACH')
        for channel_name in channel_list:
            r = self.config['color_brush_'+channel_name+'_r']
            g = self.config['color_brush_'+channel_name+'_g']
            b = self.config['color_brush_'+channel_name+'_b']
            alpha = self.config['color_brush_'+channel_name+'_alpha']
            legend_config.append( (channel_name, (r,g,b,alpha)) )
        max_length = 0
        for channel_name in channel_list:
            if len(channel_name) > max_length:
                max_length = len(channel_name)
        text_width, text_height = font.getsize('A'*max_length)
        pic_width, pic_height = text_width, text_height
        h_gap, v_gap = 7, 3
        #image = Image.new("RGBA", (h_gap*3+text_width+pic_width, h_gap*(len(channel_list)+1) + text_height*len(channel_list)) )
        #dc = ImageDraw.Draw(image)
        
        
        font_color = (0,0,0)
        start_x, start_y = self.config['draw_offset_x']+40, self.config['lattice_height']+self.config['draw_offset_y']+(self.config['image_height']-self.config['lattice_height'])/6
        
        count = 0
        for channel_name, color in legend_config:
            if count<len(channel_list)/2:
                x = count*(h_gap+text_width+pic_width)
                y = 0
            else:
                x = (count-len(channel_list)/2)*(h_gap+text_width+pic_width)
                y = v_gap + text_height
            self.dc.text( (start_x+x, start_y+y), channel_name, font_color )
            self.dc.rectangle( (start_x+x+text_width+1, start_y+y, start_x+x+text_width+pic_width+1, start_y+y+pic_height), color )
            count += 1

        #image.save("LTE_Legend.png")
    #@+node:Michael.20120322092817.1936: *4* _draw_mark
    def _draw_mark(self):
        font = self.dc.getfont()
        #author = "Author: Ling Duo, Email: duo.ling.cn@gmail.com"
        #project = "http://code.google.com/p/lte-phy-channel-on-air/"
        r, g, b, alpha = 0, 0, 0, 128
        text_width, text_height = font.getsize('A'*len(project_owner))
        pic_width, pic_height = text_width, text_height
        font_color = (0,0,0)
        start_x, start_y = self.config['draw_offset_x']+self.config['image_width']/3*2, self.config['lattice_height']+self.config['draw_offset_y']+(self.config['image_height']-self.config['lattice_height'])/6
        self.dc.text( (start_x, start_y), project_owner, font_color )
        start_y += text_height+5
        self.dc.text( (start_x, start_y), project_weblink, font_color )

    #@+node:Michael.20120322092817.1933: *4* _draw_REs
    def _draw_REs(self):
        
        start_pos = Point( 0,0 ) + self.config['draw_offset']
        for frame in range(self.config['start_SFN'],self.config['start_SFN']+self.config['frame_num']):
            for subframe in range(10):
                for l in range(7*2):
                    if self.re_size_lattice.has_key( (frame,subframe,l,0) ):
                        y = 0
                        width, height = self.re_size_lattice[(frame,subframe,l,0)]
                        width = round(width/(2048+144.)*self.config['cell_width'])
                        for k in range(self.config['N_DL_RB']*12-1,-1,-1):
                            #if self.re_size_lattice.has_key( (frame,subframe,l,k) ):
                            rect = ( start_pos.x+1, start_pos.y+y+1, start_pos.x+width-1, start_pos.y+y+height-1 )
                            self.dc.rectangle( rect, self.re_lattice[(frame,subframe,l,k)] )
                            y += self.re_size_lattice[(frame,subframe,l,k)][1]
                        start_pos += Point(width, 0)
                start_pos += Point(1,0)
            start_pos += Point(self.config['frame_interval'], 0)
                        
    #@+node:Michael.20120322092817.1930: *4* add_labels
    def add_labels(self):
        # add RB numbers on the left blank of the whole picture.
        penclr = (self.config['color_text_r'],self.config['color_text_b'],self.config['color_text_g'],self.config['color_text_alpha'])
        x = 2
        y = self.config['draw_offset'].y + self.config['RB_height'] * 0.5
        for i in range(self.config['N_DL_RB']):
            self.dc.text( (x,y), str(i), penclr )
            y += self.config['RB_height']
        
        # add slot numbers on the upper blank of the whole picture.
        x = self.config['draw_offset'].x
        y = 2
        for i in range(10*2):
            if self.config['UL_DL_S'][i/2] == 'D':
                length = self.config['DL_RB_width']
            elif self.config['UL_DL_S'][i/2] == 'U':
                length = self.config['UL_RB_width']
            else:	# 'S'
                length = self.config['special_RB_width']
            self.dc.text( (x+0.5*length,y), str(i), penclr )
            x += length
    #@+node:Michael.20120322092817.1931: *4* draw
    def draw(self, file_name):
        start_time = time()
        #print 'MainView.MainView.draw_to_bitmap starts'
        
        self._draw_lattice()
        self._draw_REs()
        self._draw_legend()
        self._draw_mark()
            
            
            #self.draw_frame( dc, deepcopy(start_pos) )
            #self.draw_frame( deepcopy(start_pos) )
            #start_pos.x += self.config['frame_width'] + self.config['frame_interval']
    #           print 'start_pos is ', start_pos
        # draw physical resource allocation
        
        #self.add_labels()
        
        #print 'in MainView.MainView.draw_to_bitmap, just before save to file.  ',time()-start_time
        
        self.image.save(file_name)
        #print 'MainView.MainView.draw_to_bitmap ends.  ',time()-start_time

    #@+node:Michael.20120322092817.1934: *4* initialize_drawer
    def initialize_drawer(self):
        
        width = 0
        for frame in range(self.config['start_SFN'],self.config['start_SFN']+self.config['frame_num']):
            for subframe in range(10):
                for l in range(2*7):
                    if self.re_size_lattice.has_key( (frame,subframe,l,0) ):
                        width += round(self.re_size_lattice[(frame,subframe,l,0)][0]/(2048+144.)*self.config['cell_width'])
                if frame==0 and subframe==0:
                    pass
                else:
                    width += 1
        self.config['lattice_width'] = int(width)
        self.config['lattice_height'] = self.config['cell_height']*self.config['N_DL_RB']*12
        self.config['image_width'] = self.config['lattice_width'] + 30
        self.config['image_height'] = self.config['lattice_height'] + 70
        
        self.image = Image.new("RGB",(self.config['image_width'],self.config['image_height']),(255,255,255))
        self.dc = ImageDraw.Draw(self.image)
        
        #self.config['RB_height'] = self.config['cell_height'] * self.config['N_RB_sc']
        #self.config['UL_RB_width'] = self.config['cell_width'] * self.config['N_UL_symb']
        #self.config['DL_RB_width'] = self.config['cell_width'] * self.config['N_DL_symb']
        #self.config['special_RB_width'] = self.config['cell_width'] * 7
        #self.config['UL_subframe_width'] = self.config['UL_RB_width'] *2
        #self.config['DL_subframe_width'] = self.config['DL_RB_width'] *2
        #self.config['special_subframe_width'] = self.config['cell_width'] *7 *2
        #self.config['frame_width'] = self.config['UL_DL_S'].count('U')*self.config['UL_subframe_width'] + self.config['UL_DL_S'].count('D')*self.config['DL_subframe_width'] + self.config['UL_DL_S'].count('S')*self.config['special_subframe_width']
        #self.config['width'] = self.config['frame_width'] * self.config['frame_num']+20
        #self.config['height'] = self.config['cell_height']*self.config['N_DL_RB']*12 +20
        
    #@-others
#@+node:Michael.20120322092817.2012: *3* class RELattice
# totally reuse dict
# key is (SFN, subframe, l, k)
# value is a color together with alpha: (R, G, B, A)
RELattice = dict

# key is also (SFN, subframe, l, k)
# value is the size of this RE in Ts
class RESizeLattice(dict):
    def __init__(self):
        dict.__init__(self)
        self.DwPTS_width, self.GAP_width, self.UpPTS_width =0,0,0
        
#@+node:Michael.20120322092817.2013: *3* class TDLTE
from numpy import floor, ceil
from math import sqrt
#import cPickle

class TDLTE:
    
    def __init__(self, config, re_lattice, re_size_lattice):
        self.config = config
        self.process_config()
        self.re_lattice = re_lattice
        self.re_size_lattice = re_size_lattice
        self.init_PHY_Common()
        
        self._init_re_size_lattice()
        self._init_re_usage_lattice()
        self._init_re_lattice()
        
        # set background for RBs
        self.set_RB_background()
        
        # set DL PHY signals and channels
        self.set_DL_PHY()
        
        # set UL PHY signals and channels
        self.set_UL_PHY()
    
    
    
    #@+others
    #@+node:Michael.20120322092817.2014: *4* Config
    #@+others
    #@+node:Michael.20120322092817.2015: *5* validate_config
    def validate_config(self):
        pass
    #@+node:Michael.20120322092817.2016: *5* process_config
    def process_config(self):
        
        # CFI_sequence
        self.config['CFIs'] = [0] * 10
        self.config['CFIs'][9] = int(self.config['CFI_sequence']%10)
        for subframe in range(1, 10):
            self.config['CFIs'][9-subframe] = int(self.config['CFI_sequence']/(10**subframe) % 10)
        self.config['CFIs'] = tuple(self.config['CFIs'])
    #@-others
    #@+node:Michael.20120322092817.2017: *4* DL_PHY
    #@+others
    #@+node:Michael.20120322092817.2018: *5* CSRS
    #@+others
    #@+node:Michael.20120322092817.2019: *6* get_CSRS_AP
    def get_CSRS_AP(self, p):
        #start_time = time()
        #print 'get_CSRS_AP starts.'

        REs = list()
        v_shift = self.config['N_cell_ID'] % 6
        for frame in range(self.config['start_SFN'],self.config['start_SFN']+self.config['frame_num']):
            for subframe in range(10):
                if self.config['UL_DL_S'][subframe] == 'D':
                    for slot in (0,1):
                        n_s = 2*subframe + slot
                        if p in (0,1):
                            ls = (0,self.config['N_DL_symb']-3)
                        else:
                            ls = (1,)
                        for l in ls:
                            if (p==0 and l==0) or (p==1 and l!=0):
                                v = 0
                            elif (p==0 and l!=0) or (p==1 and l==0):
                                v = 3
                            elif p==2:
                                v = 3 * (n_s%2)
                            elif p==3:
                                v = 3 + 3*(n_s%2)
                            for m in range(2*self.config['N_DL_RB']):
                                k = 6*m + (v+v_shift)%6
                                REs.append( (frame,subframe,l+self.config['N_DL_symb']*slot,k) )
                elif self.config['UL_DL_S'][subframe] == 'S':
                    if self.config['DwPTS'] > self.config['N_DL_symb']:
                        slot_num = 2
                    else:
                        slot_num = 1
                    for slot in range(slot_num):
                        n_s = 2*subframe + slot
                        if p in (0,1):
                            ls = (0,self.config['N_DL_symb']-3)
                        else:
                            ls = (1,)
                        for l in ls:
                            if (p==0 and l==0) or (p==1 and l!=0):
                                v = 0
                            elif (p==0 and l!=0) or (p==1 and l==0):
                                v = 3
                            elif p==2:
                                v = 3 * (n_s%2)
                            elif p==3:
                                v = 3 + 3*(n_s%2)
                            for m in range(2*self.config['N_DL_RB']):
                                k = 6*m + (v+v_shift)%6
                                if l < self.config['DwPTS'] - self.config['N_DL_symb']*slot:
                                    #self.re_usage_lattice[(frame,subframe,l+self.config['N_DL_symb']*slot,k)] = self.re_set_CSRS_AP(p)
                                    REs.append( (frame,subframe,l+self.config['N_DL_symb']*slot,k) )
        #print 'get_CSRS_AP ends.  ',time()-start_time
        return tuple(REs)
    #@+node:Michael.20120322092817.2020: *6* set_CSRS_REs
    def set_CSRS_REs(self):
        for ap in range(self.config['port_num']):
            brushclr = (self.config['color_brush_CSRS_AP'+str(ap)+'_r'], self.config['color_brush_CSRS_AP'+str(ap)+'_g'], self.config['color_brush_CSRS_AP'+str(ap)+'_b'], self.config['color_brush_CSRS_AP'+str(ap)+'_alpha'])
            for re in self.get_CSRS_AP(ap):
                self.re_lattice[re] = brushclr
        CSRS_REs = tuple()
        for ap in range(self.config['port_num']):
            CSRS_REs = CSRS_REs + self.get_CSRS_AP(ap)
        self.CSRS_REs = CSRS_REs
    #@-others
    #@+node:Michael.20120322092817.2021: *5* PBCH
    def get_PBCH_REs(self):
        start_time = time()
        #print 'get_PBCH_REs starts'
        REs = list()
        all_CSRS = self.get_CSRS_AP(0) + self.get_CSRS_AP(1) + self.get_CSRS_AP(2) + self.get_CSRS_AP(3)
        for frame in range(self.config['start_SFN'],self.config['start_SFN']+self.config['frame_num']):
            subframe = 0
            slot = 1
            for l in range(4):
                for k in range(self.config['N_DL_RB']*self.config['N_RB_sc']/2-36,self.config['N_DL_RB']*self.config['N_RB_sc']/2-36+72):
                    if (frame,subframe,l+slot*self.config['N_DL_symb'],k) not in all_CSRS:
                        REs.append( (frame,subframe,l+slot*self.config['N_DL_symb'],k) )
        #print 'get_PBCH_REs ends.  ',time()-start_time
        return tuple(REs)

    def set_PBCH_REs(self):
        self.PBCH_REs = self.get_PBCH_REs()
        brushclr = (self.config['color_brush_PBCH_r'],self.config['color_brush_PBCH_g'],self.config['color_brush_PBCH_b'],self.config['color_brush_PBCH_alpha'])
        for re in self.PBCH_REs:
            self.re_lattice[re] = brushclr

    #@+<< why force_4_port? >>
    #@+node:Michael.20120322092817.2022: *6* << why force_4_port? >>
    """
    Why do we have a argument named force_4_port?

    Because even though a system maybe composed of only 2 antenna ports, when we calculate REs occupied by PBCH, 3GPP forces us to take RS of a 4-port system into account.  So this function has such a parameter, which gives it the ability to calculate RS's REs for PBCH.
    """
    #@-<< why force_4_port? >>
    #@+node:Michael.20120322092817.2023: *5* PCFICH
    def get_PCFICH_REs(self):
        from math import floor
        #print 'get_PCFICH_REs starts'
        #start_time = time()
        REs = list()
        CSRS = self.CSRS_REs
        for frame in range(self.config['start_SFN'],self.config['start_SFN']+self.config['frame_num']):
            for subframe in range(10):
                if self.config['UL_DL_S'][subframe] in 'DS':   # this is a downlink subframe
                    l = 0
                    k_ = (self.config['N_RB_sc']/2) * (self.config['N_cell_ID'] % (2*self.config['N_DL_RB']))
                    for i in range(4):
                        k = k_ + self.config['N_RB_sc']/2* floor(self.config['N_DL_RB']/2.0*i)
                        ks = self.get_REG(l,k)
                        # after PCFICH occupies this REG, it needs to be removed from REG list
                        for k in ks:
                            if (frame,subframe,l,k) not in CSRS:
                                REs.append( (frame,subframe,l,int(k)) )
        REs = tuple(REs)
        return REs


    def set_PCFICH_REs(self):
        brushclr = (self.config['color_brush_PCFICH_r'],self.config['color_brush_PCFICH_g'],self.config['color_brush_PCFICH_b'],self.config['color_brush_PCFICH_alpha'])
        self.PCFICH_REs = self.get_PCFICH_REs()
        for re in self.PCFICH_REs:
            self.re_lattice[re] = brushclr
    #@+node:Michael.20120322092817.2024: *5* PDCCH
    def set_PDCCH_REs(self):
        brushclr = (self.config['color_brush_PDCCH_r'],self.config['color_brush_PDCCH_g'],self.config['color_brush_PDCCH_b'],self.config['color_brush_PDCCH_alpha'])
        for re in self.get_PDCCH_REs():
            self.re_lattice[re] = brushclr

    def get_PDCCH_REs(self):
        start_time = time()
        #print 'get_PDCCH_REs starts.'
        REs = tuple()
        for frame in range(self.config['start_SFN'],self.config['start_SFN']+self.config['frame_num']):
            for subframe in range(10):
                if self.config['UL_DL_S'][subframe] in 'DS':
                    #print frame,subframe
                    for reg in self.REG_dict[(frame,subframe)]:
                        REs = REs + reg
    #    print self.config['REG_indice'][(0,0,0)]
        #print 'get_PDCCH_REs ends.  ',time()-start_time
        return REs

    #@+others
    #@+node:Michael.20120322092817.2025: *6* CCE_relative
    #@+others
    #@+node:Michael.20120322092817.2026: *7* init_REG_dict
    def init_REG_dict(self):
        
        self.REG_dict = dict()
        for frame in range(self.config['start_SFN'],self.config['start_SFN']+self.config['frame_num']):
            for subframe in range(10):
                if self.config['UL_DL_S'][subframe] in 'DS':
                    self.REG_dict[(frame,subframe)] = self.get_REGs_for_subframe(frame,subframe)
    #@+node:Michael.20120322092817.2027: *7* get_REGs_for_subframe
    def get_REGs_for_subframe(self, frame, subframe):
        '''Note: this method should be called after CSRS, PCFICH, and PHICH REs have been calculated.
        initialize two dicts
            REGs: REG_index => REs
        '''
        REGs = list()
        CFI = self.config['CFIs'][subframe]
        sc_num = self.config['N_DL_RB']*self.config['N_RB_sc']
        if self.config['UL_DL_S'][subframe] in 'DS':
            k_count = [0] * CFI
            l = 0
            while min(k_count) <sc_num:
                if min(k_count) == k_count[l]:
                    # chance for this symbol to get a REG
                    re_count = 0
                    reg = [0]*4
                    k = k_count[l]
                    while re_count<4 and k<=sc_num:
                        re = (frame,subframe,l,k)
                        if (re in self.CSRS_REs) or (re in self.PCFICH_REs) or (re in self.PHICH_REs) or (re in self.PSS_REs):
                            pass
                        else:   # this RE isn't used by anyone
                            reg[re_count] = re
                            re_count += 1
                        k += 1
                    if re_count == 4:
                        re_count = 0
                        REGs.append(tuple(reg))
                        k_count[l] = k
                l = (l+1)%CFI
        return tuple(REGs)
    #@+node:Michael.20120322092817.2028: *7* search_space
    def get_PDCCH_common_search_space(self, L, N_CCE_k):
        Y_k = 0
        if L ==4 :
            M_L = 4
        elif L == 8:
            M_L = 2
        CCE_indices = list()
        for i in range(L):
            for m in range(M_L):
                CCE_indices.append( L*((Y_k+m)%(N_CCE_k/L))+i )
        CCE_indices.sort()
        return tuple(CCE_indices)

    def get_PDCCH_UE_specific_search_space(self, n_s, n_RNTI, L, N_CCE_k):
        A = 39827
        D = 65537
        k = n_s/2
        Y_k = self.Y_sequence(n_RNTI,k)
        if L in (1,2):
            M_L = 6
        elif L in (4,8):
            M_L = 2
        CCE_indices = list()
        for m in range(M_L):
            for i in range(L):
                CCE_indices.append( L*((Y_k+m)%(N_CCE_k/L))+i )
        CCE_indices.sort()
        return tuple(CCE_indices)
        
    def Y_sequence(self, n_RNTI, k):
        # if n_RNTI==0, a error should be raised
        D = 65537
        A = 39827
        if k == -1:
            return n_RNTI
        else:
            return (A*self.Y_sequence(n_RNTI,k-1)) % D
    #@-others

    #@+node:Michael.20120322092817.2029: *6* get_all_REG_in_symbol
    def get_all_REG_in_symbol(self,frame,subframe,l):

        REGs = list()
        if l == 0:
            for k in range( self.config['N_DL_RB']*self.config['N_RB_sc']/6 ):
                tmp_reg = list()
                tmp_reg.append( (frame,subframe,l,6*k) )
                tmp_reg.append( (frame,subframe,l,6*k+1) )
                tmp_reg.append( (frame,subframe,l,6*k+2) )
                tmp_reg.append( (frame,subframe,l,6*k+3) )
                tmp_reg.append( (frame,subframe,l,6*k+4) )
                tmp_reg.append( (frame,subframe,l,6*k+5) )
                REGs.append(tmp_reg)
        elif l == 1:
            if self.config['port_num'] == 2:
                for k in range( self.config['N_DL_RB']*self.config['N_RB_sc']/4 ):
                    REGs.append( (frame,subframe,l,6*k) )
                    REGs.append( (frame,subframe,l,6*k+1) )
                    REGs.append( (frame,subframe,l,6*k+2) )
                    REGs.append( (frame,subframe,l,6*k+3) )
            elif self.config['port_num'] ==4:
                for k in range( self.config['N_DL_RB']*self.config['N_RB_sc']/6 ):
                    REGs.append( (frame,subframe,l,6*k) )
                    REGs.append( (frame,subframe,l,6*k+1) )
                    REGs.append( (frame,subframe,l,6*k+2) )
                    REGs.append( (frame,subframe,l,6*k+3) )
                    REGs.append( (frame,subframe,l,6*k+4) )
                    REGs.append( (frame,subframe,l,6*k+5) )
        elif l == 2:
            for k in range( self.config['N_DL_RB']*self.config['N_RB_sc']/4 ):
                REGs.append( (frame,subframe,l,6*k) )
                REGs.append( (frame,subframe,l,6*k+1) )
                REGs.append( (frame,subframe,l,6*k+2) )
                REGs.append( (frame,subframe,l,6*k+3) )
        elif l == 3:
                if self.config['CP_DL_type'] == 0:    # for nomal CP
                    for k in range( self.config['N_DL_RB']*self.config['N_RB_sc']/4 ):
                        REGs.append( (frame,subframe,l,6*k) )
                        REGs.append( (frame,subframe,l,6*k+1) )
                        REGs.append( (frame,subframe,l,6*k+2) )
                        REGs.append( (frame,subframe,l,6*k+3) )
                else:
                    for k in range( self.config['N_DL_RB']*self.config['N_RB_sc']/6 ):
                        REGs.append( (frame,subframe,l,6*k) )
                        REGs.append( (frame,subframe,l,6*k+1) )
                        REGs.append( (frame,subframe,l,6*k+2) )
                        REGs.append( (frame,subframe,l,6*k+3) )
                        REGs.append( (frame,subframe,l,6*k+4) )
                        REGs.append( (frame,subframe,l,6*k+5) )

        return REGs




    #@-others
    #@+node:Michael.20120322092817.2030: *5* PHICH
    def set_PHICH_REs(self):
        self.PHICH_REs = self.get_PHICH_REs()
        brushclr = (self.config['color_brush_PHICH_r'],self.config['color_brush_PHICH_g'],self.config['color_brush_PHICH_b'],self.config['color_brush_PHICH_alpha'])
        for re in self.PHICH_REs:
            self.re_lattice[re] = brushclr

    def get_PHICH_REs(self):
        #start_time = time()
        #print 'PHICH.get_REs starts.'
        REs = list()
        N_g = (1./6, 1./2, 1, 2)
    #    print "N_g is ", N_g[int(self.config['N_g'])]
        N_group_PHICH = int( ceil( N_g[int(self.config['N_g'])] * ( self.config['N_DL_RB']/8. ) ) )
        #print 'in PHICH, befor entering the first for loop.  ',time()-start_time
        for frame in range(self.config['start_SFN'],self.config['start_SFN']+self.config['frame_num']):
            #print 'in PHICH, in the first for loop, frame=%d  '%frame,time()-start_time
            # calculation of m_i, refer to table 6.9-1 in 36.211
            for subframe in range(10):
                if self.config['UL_DL_config'] == 0:
                    if subframe in (0,5):
                        m_i = 2
                    elif subframe in (1,6):
                        m_i = 1
                    else:
                        m_i = 0
                elif self.config['UL_DL_config'] == 1:
                    if subframe in (1,4,6,9):
                        m_i = 1
                    else:
                        m_i = 0
                elif self.config['UL_DL_config'] == 2:
                    if subframe in (3,8):
                        m_i = 1
                    else:
                        m_i = 0
                elif self.config['UL_DL_config'] == 3:
                    if subframe in (0,8,9):
                        m_i = 1
                    else:
                        m_i = 0
                elif self.config['UL_DL_config'] == 4:
                    if subframe in (8,9):
                        m_i = 1
                    else:
                        m_i = 0
                elif self.config['UL_DL_config'] == 5:
                    if subframe == 8:
                        m_i = 1
                    else:
                        m_i = 0
                elif self.config['UL_DL_config'] == 6:
                    if subframe in (0,1,5,6,9):
                        m_i = 1
                    else:
                        m_i = 0
                slot = 0
                for l_ in range(self.config['CFI']):
                    n_l = len( self.config['REG_indice'][(frame,subframe,l_)] )
    #                print l,n_l
    #                print m_i,N_group_PHICH
                    for m in range( m_i*N_group_PHICH ):
    #                    print m,
                        for i in (0,1,2):
                            if self.config['PHICH_duration'] == 0:
                                l = 0
                            elif self.config['PHICH_duration'] == 1 and subframe in (1,6):
                                l = ( 1 + i + int(floor(m/2.)) ) % 2
                            else:
                                l = i
                            n_cur = len( self.config['REG_indice'][(frame,subframe,l)] )
                            n_0 = len( self.config['REG_indice'][(frame,subframe,0)] )
                            n_1 = len( self.config['REG_indice'][(frame,subframe,1)] )
                            if self.config['PHICH_duration'] == 1 and subframe in (1,6):
                                if i == 0:
                                    n = floor(self.config['N_cell_ID'] * n_cur / n_0 + m) % n_cur
                                elif i == 1:
                                    n = floor(self.config['N_cell_ID'] * n_cur / n_0 + m + floor(n_cur/3.)) % n_cur
                                elif i == 2:
                                    n = floor(self.config['N_cell_ID'] * n_cur / n_0 + m + floor(2*n_cur/3.)) % n_cur
                            else:
                                if i == 0:
                                    n = floor(self.config['N_cell_ID'] * n_cur / n_0 + m) % n_cur
                                elif i == 1:
                                    n = floor(self.config['N_cell_ID'] * n_cur / n_0 + m + floor(n_cur/3.)) % n_cur
                                elif i == 2:
                                    n = floor(self.config['N_cell_ID'] * n_cur / n_0 + m + floor(2*n_cur/3.)) % n_cur
                            n = int(n)
                            res = self.REG_index_to_REs(frame,subframe,l,self.config['REG_indice'][(frame,subframe,l)][n])
                            for re in res:
                                REs.append(re)
        
        REG_indice = dict()
        #print 'in PHICH, print 2:  ',time()-start_time
        for re in REs:
            frame,subframe,l,k = re
            if (frame,subframe,l) not in REG_indice.keys():
                REG_indice[(frame,subframe,l)] = list()
                REG_indice[(frame,subframe,l)].append( self.RE_to_REG_index(re) )
            else:
                tmp_REG_index = self.RE_to_REG_index(re)
                if tmp_REG_index not in REG_indice[(frame,subframe,l)]:
                    REG_indice[(frame,subframe,l)].append( tmp_REG_index )
        for key in REG_indice.keys():
            for index in REG_indice[key]:
                self.config['REG_indice'][key].remove(index)
        #print 'PHICH.get_REs ends.  ',time()-start_time
        return tuple(REs)
        


    #@+node:Michael.20120322092817.2031: *6* phich
    def channel_code_HI(self, HI):
        return ((0,0,0),(1,1,1))[HI]

    def phich(self, HI, n_s, n_group_PHICH, n_seq_PHICH):
        # one bit input: 1 for ACK, 0 for NACK
        
        # channel coding
        b = self.channel_code_HI(HI)
        M_bit = M_s = 3
        
        # modulation
        z = [0] * M_s
        for i in range(M_bit):
            z[i] = self.BPSK(b[i])
        
        if self.config['CP_DL_type'] == 0:
            N_PHICH_SF = 4  # for normal CP
        else:
            N_PHICH_SF = 2  # for extended CP
        
        # 8 orthorgonal sequences for normal CP
        orth_seq_NCP = ( (+1,+1,+1,+1),  (+1,-1,+1,-1),    (+1,+1,-1,-1),    (+1,-1,-1,+1),
                                     (+j,+j,+j,+j), (+j,-j,+j,-j),  (+j,+j,-j,-j),  (+j,-j,-j,+j) )
        # 4 orthorgonal sequences for extended CP
        orth_seq_ECP = ( (+1,+1),    (+1,-1),    (+j,+j),    (+j,-j) )
        
        # bit-wise multiplied with an orthogonal sequence (should be scrambled, but not implemented here)
        M_symb = N_PHICH_SF * M_s
        d = [0] * M_symb
        c_init = (n_s/2+1) * (2*self.config['N_cell_ID']+1)* 2**9 + self.config['N_cell_ID']
        for i in range(M_symb):
            d[i] = orth_seq[n_seq_PHICH][i%N_PHICH_SF] * (1-2*self.c(c_init,i)) * z[i/4]
        
        # REG alignment
        if self.config['CP_DL_type'] == 0:
            d_0 = d  # for normal CP
        else:
            # for extended CP
            d_0 = [0] * 2 * M_symb
            for i in range(M_symb/2):
                if n_group_PHICH%2==0:
                    d_0[4*i], d_0[4*i+1], d_0[4*i+2], d_0[4*i+3] = d[2*i], d[2*i+1], 0, 0
                else:
                    # n_group_PHICH%2==1
                    d_0[4*i], d_0[4*i+1], d_0[4*i+2], d_0[4*i+3] = 0, 0, d[2*i], d[2*i+1]
        
        # layer mapping.
        # TODO: refer to section 6.9.2 in 36.211. Check the code below
        x = numpy.matrix( '0 0 0 0 0 0; 0 0 0 0 0 0' )
        tmp = x.tolist()
        for i in range(6):
            for j in range(2):
    #            print i*2 + j
                tmp[j][i] = d[i*j+j]
        x = tmp
        
        # precoding
        y = numpy.matrix( '0 0 0 0 0 0 0 0 0 0 0 0; 0 0 0 0 0 0 0 0 0 0 0 0' )
        y = y.tolist()
        for i in range(6):
            y[0][2*i] = sqrt(2)/2 * ( real(x[0][i]) + complex(0,1)*complex(0,1)*imag(x[0][i]) )
        for i in range(6):
            y[1][2*i] = sqrt(2)/2 * ( -1*real(x[1][i]) + complex(0,1)*complex(0,1)*imag(x[1][i]) )
        for i in range(6):
            y[0][2*i+1] = sqrt(2)/2 * ( real(x[1][i]) + complex(0,1)*complex(0,1)*imag(x[1][i]) )
        for i in range(6):
            y[1][2*i+1] = sqrt(2)/2 * ( real(x[0][i]) + complex(0,-1)*complex(0,1)*imag(x[0][i]) )
        return y
        
        
        
    #@+node:Michael.20120322092817.2032: *5* PSS
    def get_PSS_REs(self):
        #start_time = time()
        #print 'get_PSS_REs starts'
        REs = list()
        for frame in range(self.config['start_SFN'],self.config['start_SFN']+self.config['frame_num']):
            for subframe in (1,6):
                l = 3-1
                for n in range(-5,67):
                    k = n-31 + self.config['N_DL_RB']*self.config['N_RB_sc']/2
                    REs.append( (frame,subframe,l,k) )
        #print 'get_PSS_REs ends.  ',time()-start_time
        return tuple(REs)
        
    def set_PSS_REs(self):
        self.PSS_REs = self.get_PSS_REs()
        brushclr = (self.config['color_brush_PSS_r'],self.config['color_brush_PSS_g'],self.config['color_brush_PSS_b'],self.config['color_brush_PSS_alpha'])
        for re in self.PSS_REs:
            self.re_lattice[re] = brushclr
            #print re
        #self.dump_lattice()
    #@+node:Michael.20120322092817.2033: *5* SSS
    def get_SSS_REs(self):
        '''
        Return all SSS REs.
        '''
        #start_time = time()
        #print 'get_SSS_REs starts.'
        REs = list()
        for frame in range(self.config['start_SFN'],self.config['start_SFN']+self.config['frame_num']):
            for subframe in (0,5):
                l = self.config['N_DL_symb']-1
                for n in range(-5,67):
                    k = n-31 + self.config['N_DL_RB']*self.config['N_RB_sc']/2
                    REs.append( (frame,subframe,l+self.config['N_DL_symb'],k) )
        #print 'get_SSS_REs ends.  ',time()-start_time
        return tuple(REs)

    def set_SSS_REs(self):
        self.SSS_REs = self.get_SSS_REs()
        brushclr = (self.config['color_brush_SSS_r'],self.config['color_brush_SSS_g'],self.config['color_brush_SSS_b'],self.config['color_brush_SSS_alpha'])
        for re in self.SSS_REs:
            self.re_lattice[re] = brushclr
    #@-others


    def set_DL_PHY(self):
        
        self.REG_nums = dict()
        for frame in range(self.config['start_SFN'],self.config['start_SFN']+self.config['frame_num']):
            for subframe in range(10):
                if self.config['UL_DL_S'][subframe] in 'DS':
                    for l in (0,1,2,3):
                        self.REG_nums[(frame,subframe,l)] = self.get_all_REG_in_symbol(frame,subframe,l)
        self.config['REG_nums'] = self.REG_nums
        self.config['REG_indice'] = self.get_REG_indice()
        
        self.set_CSRS_REs()
        self.set_PSS_REs()
        self.set_SSS_REs()
        self.set_PBCH_REs()
        self.set_PCFICH_REs()
        
        # a temporary work-around to fix PHICH occupies PCFICH REs problem
        for i in range(len(self.PCFICH_REs)/4):
            re = self.PCFICH_REs[4*i]
            frame, subframe, l, k = re
            reg_index = self.RE_to_REG_index(re)
            tmp_index = self.config['REG_indice'][(frame,subframe,l)].index(reg_index)
            del( self.config['REG_indice'][(frame,subframe,l)][tmp_index] )
            
            for j in range(len(self.config['REG_nums'][(frame,subframe,l)])-1, -1, -1):
                if re in self.config['REG_nums'][(frame,subframe,l)][j]:
                    del( self.config['REG_nums'][(frame,subframe,l)][j] )
        # end of this temporary work-around
        
        
        self.set_PHICH_REs()
        
        self.init_REG_dict()
        self.set_PDCCH_REs()
        
        #self.dump_lattice()
    #@+node:Michael.20120322092817.2034: *4* Helper_methods
    #@+others
    #@+node:Michael.20120322092817.2035: *5* dump_lattice
    def dump_lattice(self):
        start_time = time()
        # dump self.re_size_lattice
        f = open("re_size_lattice.txt",'w')
        for sfn in range(self.config['start_SFN'],self.config['start_SFN']+self.config['frame_num']):
            for subframe in range(10):
                for l in range(2*self.config['N_DL_symb']):
                    for k in range(12*self.config['N_DL_RB']):
                        if self.re_size_lattice.has_key( (sfn,subframe,l,k) ):
                            f.write( str((sfn,subframe,l,k)) + ':' + str(self.re_size_lattice[(sfn,subframe,l,k)]) )
                            f.write('\t')
                f.write('\n')
        f.close()
        
        # dump self.re_lattice
        f = open("re_lattice.txt",'w')
        for sfn in range(self.config['start_SFN'],self.config['start_SFN']+self.config['frame_num']):
            for subframe in range(10):
                for l in range(2*self.config['N_DL_symb']):
                    for k in range(12*self.config['N_DL_RB']):
                        if self.re_lattice.has_key( (sfn,subframe,l,k) ):
                            f.write( str((sfn,subframe,l,k)) + ':' + str(self.re_lattice[(sfn,subframe,l,k)]) )
                            f.write('\t')
                f.write('\n')
        f.close()
        print 'dump_lattice consumed: ', time()-start_time
    #@+node:Michael.20120322092817.2036: *5* get_REG
    def get_REG(self,l,k):
        ks = list()
        if l == 0:
            ks.append(k/6*6)
            ks.append(k/6*6+1)
            ks.append(k/6*6+2)
            ks.append(k/6*6+3)
            ks.append(k/6*6+4)
            ks.append(k/6*6+5)
        elif l == 1:
            if self.config['port_num'] == 2:
                ks.append(k/4*4)
                ks.append(k/4*4+1)
                ks.append(k/4*4+2)
                ks.append(k/4*4+3)
            elif self.config['port_num'] ==4:
                ks.append(k/6*6)
                ks.append(k/6*6+1)
                ks.append(k/6*6+2)
                ks.append(k/6*6+3)
                ks.append(k/6*6+4)
                ks.append(k/6*6+5)
        elif l == 2:
            ks.append(k/4*4)
            ks.append(k/4*4+1)
            ks.append(k/4*4+2)
            ks.append(k/4*4+3)
        elif l == 3:
                if self.config['CP_DL_type'] == 0:    # for nomal CP
                    ks.append(k/4*4)
                    ks.append(k/4*4+1)
                    ks.append(k/4*4+2)
                    ks.append(k/4*4+3)
                else:
                    ks.append(k/6*6)
                    ks.append(k/6*6+1)
                    ks.append(k/6*6+2)
                    ks.append(k/6*6+3)
                    ks.append(k/6*6+4)
                    ks.append(k/6*6+5)
        return ks

    #@+node:Michael.20120322092817.2037: *5* get_REG_indice
    def get_REG_indice(self):
        #start_time = time()
        indice = dict()
        for frame in range(self.config['start_SFN'],self.config['start_SFN']+self.config['frame_num']):
            for subframe in range(10):
                for l in range(3):
                    indice[(frame,subframe,l)] = self.get_REG_indice_in_symbol(frame,subframe,l)
    	#print 'get_REG_indice consumed: ', time()-start_time
        return indice
    #@+node:Michael.20120322092817.2038: *5* get_REG_indice_in_symbol
    def get_REG_indice_in_symbol(self,frame,subframe,l):
        indice = list()
        count = self.how_many_RE_per_REG(frame,subframe,l)
        tmp = 0
        while tmp*count <self.config['N_DL_RB']*self.config['N_RB_sc']:
            indice.append(tmp)
            tmp += 1
        return indice
    #@+node:Michael.20120322092817.2039: *5* how_many_RE_per_REG
    def how_many_RE_per_REG(self,frame,subframe,l):
        '''
        Return the number of REs per REG in symbol l of (frame, subframe).
        '''
        slot = subframe*2 + l/self.config['N_DL_symb']
        l = l%self.config['N_DL_symb']
        count = 0
        if l == 0:
            count = 6
        elif l == 1:
            if self.config['port_num'] == 2:
                count = 4
            elif self.config['port_num'] ==4:
                count = 6
        elif l == 2:
            count = 4
        elif l == 3:
            if self.config['CP_DL_type'] == 0:    # for nomal CP
                count = 4
            else:
                count = 6
        return count
    #@+node:Michael.20120322092817.2040: *5* init_REG
    def init_REG_tables(self):
        self.init_REG_RE2index_in_symbol()
        self.init_REG_RE2index_in_subframe()



    def init_REG_RE2index_in_symbol(self):
        pass


    def init_REG_RE2index_in_subframe(self):
        pass
    #@+node:Michael.20120322092817.2041: *5* myfloor
    def myfloor(self, x):
        x = numpy.floor(x)
        return int(x)

    #@+node:Michael.20120322092817.2042: *5* phich
    def phich( x, seq_index ):
        # one bit input
        
        # channel coding
        if x == 1:
            x = [1,1,1]
        elif x == 0:
            x = [0,0,0]
        
        # modulation
        for i in range(3):
            if x[i] == 1:
                x[i] = complex( sqrt(2)/2,sqrt(2)/2 )
            elif x[i] == 0:
                x[i] = complex( sqrt(2)/(-2),sqrt(2)/(-2) )
        
        orth_seq = ( (1,1,1,1), (1,-1,1,-1), (1,1,-1,-1), (1,-1,-1,1), (complex(0,1),complex(0,1),complex(0,1),complex(0,1)), (complex(0,1),complex(0,-1),complex(0,1),complex(0,-1)), (complex(0,1),complex(0,1),complex(0,-1),complex(0,-1)), (complex(0,1),complex(0,-1),complex(0,-1),complex(0,1)) )
        d = list()
        for i in range(12):
    #        print i%4, i/4
            d.append( x[i/4] * orth_seq[seq_index][i%4] )
        
        # layer mapping
        x = numpy.matrix( '0 0 0 0 0 0; 0 0 0 0 0 0' )
        tmp = x.tolist()
        for i in range(6):
            for j in range(2):
    #            print i*2 + j
                tmp[j][i] = d[i*j+j]
        x = tmp
        
        # precoding
        y = numpy.matrix( '0 0 0 0 0 0 0 0 0 0 0 0; 0 0 0 0 0 0 0 0 0 0 0 0' )
        y = y.tolist()
        for i in range(6):
            y[0][2*i] = sqrt(2)/2 * ( real(x[0][i]) + complex(0,1)*complex(0,1)*imag(x[0][i]) )
        for i in range(6):
            y[1][2*i] = sqrt(2)/2 * ( -1*real(x[1][i]) + complex(0,1)*complex(0,1)*imag(x[1][i]) )
        for i in range(6):
            y[0][2*i+1] = sqrt(2)/2 * ( real(x[1][i]) + complex(0,1)*complex(0,1)*imag(x[1][i]) )
        for i in range(6):
            y[1][2*i+1] = sqrt(2)/2 * ( real(x[0][i]) + complex(0,-1)*complex(0,1)*imag(x[0][i]) )
        return y
        
        
        
    #@+node:Michael.20120322092817.2043: *5* RE_to_REG_index
    def RE_to_REG_index(self,re):
        frame,subframe,l,k = re
        count = self.how_many_RE_per_REG(frame,subframe,l)
        return k/count
    #@+node:Michael.20120322092817.2044: *5* REG_index_to_REs
    def REG_index_to_REs(self,frame,subframe,l,REG_index):
        #slot = 2*subframe + l/self.config['N_DL_symb']
        #l = l%self.config['N_DL_symb']
        REs = list()
        count = self.how_many_RE_per_REG(frame,subframe,l)
        csrs = self.CSRS_REs
        for i in range(count):
            if (frame,subframe,l,count*REG_index+i) not in csrs:
                REs.append( (frame,subframe,l,count*REG_index+i) )
        return REs
    #@+node:Michael.20120322092817.2045: *5* set_RB_background
    def set_RB_background(self):
        
        for sfn in range(self.config['start_SFN'],self.config['start_SFN']+self.config['frame_num']):
            for subframe in range(10):
                if self.config['UL_DL_S'][subframe] == 'D':
                    # this is a downlink subframe
                    for l in range(2*self.config['N_DL_symb']):
                        for k in range(12*self.config['N_DL_RB']):
                            if (l%(2*self.config['N_DL_symb'])<self.config['N_DL_symb'] and (k/12)%2==0) or (l%(2*self.config['N_DL_symb'])>=self.config['N_DL_symb'] and (k/12)%2==1):
                                self.re_lattice[(sfn,subframe,l,k)] = ( self.config['color_brush1_RB_r'], self.config['color_brush1_RB_g'], self.config['color_brush1_RB_b'], self.config['color_brush1_RB_alpha'] )
                elif self.config['UL_DL_S'][subframe] == 'U':
                    # this is a uplink subframe
                    for l in range(2*self.config['N_UL_symb']):
                        for k in range(12*self.config['N_UL_RB']):
                            if (l%(2*self.config['N_UL_symb'])<self.config['N_UL_symb'] and (k/12)%2==0) or (l%(2*self.config['N_UL_symb'])>=self.config['N_UL_symb'] and (k/12)%2==1):
                                self.re_lattice[(sfn,subframe,l,k)] = ( self.config['color_brush1_RB_r'], self.config['color_brush1_RB_g'], self.config['color_brush1_RB_b'], self.config['color_brush1_RB_alpha'] )
                else:
                    # this is a special subframe
                    pass
    #@+node:Michael.20120322092817.2046: *5* set_REG_num
    def set_REG_num(self):
        '''
        This function should be called only once!
        '''
        REG_num = list()
        REG_num.append( 2*self.config['N_DL_RB'] )  # for symbol 0
        if self.config['port_num'] == 2:    # for symbol 1
            REG_num.append( 3*self.config['N_DL_RB'] )
        else:
            REG_num.append( 2*self.config['N_DL_RB'] )
        REG_num.append( 3*self.config['N_DL_RB'] )    # for symbol 2
        if self.config['CP_DL_type'] == 0:    # for symbol 3
            REG_num.append( 3*self.config['N_DL_RB'] )
        else:
            REG_num.append( 2*self.config['N_DL_RB'] )

        return REG_num
    #@+node:Michael.20120322092817.2047: *5* ts_to_pixel
    def ts_to_pixel(self,len_in_ts):
        return round(len_in_ts/(2048+144.)*self.config['cell_width'])
    #@-others
    #@+node:Michael.20120322092817.2048: *4* PHY_Common
    def init_PHY_Common(self):    
        self.init_BPSK()
        self.init_QPSK()
        self.init_16QAM()
        self.init_64QAM()

    #@+others
    #@+node:Michael.20120322092817.2049: *5* 16QAM
    def QAM16(self, (b0,b1,b2,b3)):
        return self.QAM16[b3+2*b2+4*b1+8*b0]

    def init_16QAM(self):
        I = Q = 1/sqrt(10)
        self.QAM16 = (  complex(1*I, 1*Q),
                                complex(1*I, 3*Q),
                                complex(3*I, 1*Q),
                                complex(3*I, 3*Q),
                                complex(1*I, -1*Q),
                                complex(1*I, -3*Q),
                                complex(3*I, -1*Q),
                                complex(3*I, -3*Q),
                                complex(-1*I, 1*Q),
                                complex(-1*I,3*Q),
                                complex(-3*I, 1*Q),
                                complex(-3*I, 3*Q),
                                complex(-1*I, -1*Q),
                                complex(1*I, -3*Q),
                                complex(-3*I, -1*Q),
                                complex(-3*I, -3*Q),
        )
    #@+node:Michael.20120322092817.2050: *5* 64QAM
    def QAM64(self, (b0,b1,b2,b3,b4,b5)):
        return self.QAM64[b5+b4*2+b3*4+b2*8+b1*16+b0*32]


    def init_64QAM(self):
        tmp_64QAM = [0] * 64
        I = Q = 1/sqrt(42)
        tmp_list = (    (3,3), (3,1), (1,3), (1,1), (3,5), (3,7), (1,5), (1,7),
                            (5,3), (5,1), (7,3), (7,1), (5,5), (5,7), (7,5), (7,7),
                            (3,-3), (3,-1), (1,-3), (1,-1), (3,-5), (3,-7), (1,-5),(1,-7),
                            (5,-3), (5,-1), (7,-3), (7,-1), (5,-5), (5,-7), (7,-5), (7,-7),
                            (-3,3), (-3,1), (-1,3), (-1,1), (-3,5), (-3,7), (-1,5), (-1,7),
                            (-5,3), (-5,1), (-7,3), (-7,1), (-5,5), (-5,7), (-7,5), (-7,7),
                            (-3,-3), (-3,-1), (-1,-3),(-1,-1), (-3,-5), (-3,-7), (-1,-5), (-1,-7),
                            (-5,-3), (-5,-1), (-7,-3), (-7,-1), (-5,-5), (-5,-7), (-7,-5), (-7,-7) )
        for k in range(len(tmp_list)):
            i,q = tmp_list[k]
            tmp_64QAM[k] = complex( i*I, q*Q )
        self.QAM64 = tuple(tmp_64QAM)
    #@+node:Michael.20120322092817.2051: *5* _init_re_size_lattice
    def _init_re_size_lattice(self):
        for sfn in range(self.config['start_SFN'],self.config['start_SFN']+self.config['frame_num']):
            for subframe in range(10):
                if self.config['UL_DL_S'][subframe] == 'D':
                    # this is a downlink subframe
                    for l in range(2*self.config['N_DL_symb']):
                        for k in range(12*self.config['N_DL_RB']):
                            if self.config['CP_DL_type'] == 0:
                                # normal CP
                                if l==0:
                                    width = 160+2048
                                else:
                                    width = 144+2048
                            else:
                                # extended CP
                                width = 512+2048
                            self.re_size_lattice[(sfn,subframe,l,k)] = (width,self.config['cell_height'])
                elif self.config['UL_DL_S'][subframe] == 'U':
                    # this is a uplink subframe
                    for l in range(2*self.config['N_UL_symb']):
                        for k in range(12*self.config['N_UL_RB']):
                            if self.config['CP_UL_type'] == 0:
                                # normal CP
                                if l==0:
                                    width = 160+2048
                                else:
                                    width = 144+2048
                            else:
                                # extended CP
                                width = 512+2048
                            self.re_size_lattice[(sfn,subframe,l,k)] = (width,self.config['cell_height'])
                else:   # S
                    # this is a special subframe
                    # this is tricky, and here we treat the GAP as one symbol
                    # DwPTS
                    for k in range(12*self.config['N_DL_RB']):
                        if self.config['CP_DL_type'] == 0:
                                # normal CP in DL
                                # set DL symbols
                                self.re_size_lattice[(sfn,subframe,0,k)] = (160+2048,self.config['cell_height'])
                                for l in range(1,self.get_DwPTS_symbol_num()):
                                    self.re_size_lattice[(sfn,subframe,l,k)] = (144+2048,self.config['cell_height'])
                        else:
                            # extended CP in DL
                            # set DL symbols
                            for l in range(self.get_DwPTS_symbol_num()):
                                self.re_size_lattice[(sfn,subframe,l,k)] = (512+2048,self.config['cell_height'])
                    # GAP
                    for k in range(12*self.config['N_DL_RB']):
                        self.re_size_lattice[(sfn,subframe,self.get_DwPTS_symbol_num(),k)] = (self.get_GAP_Ts(),self.config['cell_height'])
                    # UpPTS
                    for k in range(12*self.config['N_DL_RB']):
                        if self.config['CP_UL_type'] == 0:
                            # normal CP in UL
                            for l in range(self.get_UpPTS_symbol_num()):
                                self.re_size_lattice[(sfn,subframe,l+self.get_DwPTS_symbol_num()+1,k)] = (144+2048,self.config['cell_height'])
                        else:
                            # extended CP in UL
                            for l in range(self.get_UpPTS_symbol_num()):
                                self.re_size_lattice[(sfn,subframe,l+self.get_DwPTS_symbol_num()+1,k)] = (512+2048,self.config['cell_height'])
        
        self.re_size_lattice.DwPTS_width = self.ts_to_pixel(self.get_DwPTS_Ts())
        self.re_size_lattice.GAP_width = self.ts_to_pixel(self.get_GAP_Ts())
        self.re_size_lattice.UpPTS_width = self.ts_to_pixel(self.get_UpPTS_Ts())
    #@+node:Michael.20120322092817.2052: *5* _init_re_lattice
    def _init_re_lattice(self):
        color = (self.config['color_brush_RE_r'], self.config['color_brush_RE_g'], self.config['color_brush_RE_b'], self.config['color_brush_RE_alpha'])
        s_color = (self.config['color_brush_S_RE_r'], self.config['color_brush_S_RE_g'], self.config['color_brush_S_RE_b'], self.config['color_brush_S_RE_alpha'])
        for k in self.re_size_lattice.keys():
            if self.config['UL_DL_S'][k[1]] == 'S':
                self.re_lattice[k] = s_color
            else:
                self.re_lattice[k] = color
    #@+node:Michael.20120322092817.2053: *5* _init_re_usage_lattice
    def _init_re_usage_lattice(self):
        '''
        A bitwise interpretated integer:
            default: all 0 => blank
            bit0:   1 for CSRS
            bit2-1: Antenna Port Number
            bit3:   1 for PSS
            bit4:   1 for SSS
            bit5:   1 for PBCH
            bit6:   1 for PCFICH
            bit7:   1 for PHICH
            bit8:   1 for PDCCH
            bit16-9:    CCE index (8 bit)
            bit26-17:   REG index (10 bit)
            bit27:   1 for PRACH
        '''
        self.re_usage_lattice = RELattice()
        
        # constants
        self.RE_USAGE_BLANK = 0
        self.RE_USAGE_CSRS = 1
        self.RE_USAGE_PSS = 1>>3
        self.RE_USAGE_SSS = 1>>4
        self.RE_USAGE_PBCH = 1>>5
        self.RE_USAGE_PCFICH = 1>>6
        self.RE_USAGE_PHICH = 1>>7
        self.RE_USAGE_PDCCH = 1>>8
        
        # initialize RE usage lattice
        for k in self.re_size_lattice.keys():
            self.re_usage_lattice[k] = self.RE_USAGE_BLANK

    def re_set_CSRS_AP(self, ap_num):
        return 1 ^ ap_num<<1

    def re_get_CSRS_AP(self, x):
        return (x>>1)&3

    def re_set_CCE_index(self, x, cce_index):
        return x ^ cce_index<<9

    def re_set_REG_index(self, x, reg_index):
        return x ^ reg_index<<17

    def re_get_PDCCH_CCE_index(self, x):
        return (x>>9)&255

    def re_get_PDCCH_REG_index(self, x):
        return (x>>17)&1023

    def re_is_blank(self, x):
        return x==0

    def re_is_CSRS(self, x):
        return bool(x & 1)

    def re_is_PSS(self, x):
        return bool( (x>>3)&1 )
        
    def re_is_SSS(self, x):
        return bool( (x>>4)&1 )

    def re_is_PBCH(self, x):
        return bool( (x>>5)&1 )

    def re_is_PCFICH(self, x):
        return bool( (x>>6)&1 )

    def re_is_PHICH(self, x):
        return bool( (x>>7)&1 )

    def re_is_PDCCH(self, x):
        return bool( (x>>8)&1 )

    def re_is_PRACH(self, x):
        return bool( (x>>27)&1 )
    #@+node:Michael.20120322092817.2054: *5* BPSK
    def BPSK(self, b):
        # one bit modulation
        return self.BPSK[b]

    def init_BPSK(self):
        self.BPSK = ( complex( 1/sqrt(2), 1/sqrt(2) ), complex( -1/sqrt(2), -1/sqrt(2) ) )
    #@+node:Michael.20120322092817.2055: *5* c
    def c(self, c_init, i):
        N_C = 1600
        return (self.x_1(i+N_C) + self.x_2(c_init,i+N_C)) %2
    #@+node:Michael.20120322092817.2056: *5* QPSK
    def QPSK(self, (b0,b1)):
        return self.QPSK[2*b0+b1]

    def init_QPSK(self):
        self.QPSK = ( complex(1/sqrt(2),1/sqrt(2)), complex(1/sqrt(2),-1/sqrt(2)),
                            complex(-1/sqrt(2),1/sqrt(2)), complex(-1/sqrt(2),-1/sqrt(2))
        )
    #@+node:Michael.20120322092817.2057: *5* x_1
    def x_1(self, i):
        x1_init = 1
        while i>30:
            tmp = (x1_init&1 ^ x1_init&8)%2
            x1_init = x1_init>>1 ^ tmp*(2**30)
            i -= 1
        return (x1_init >> i) & 1

    #@+node:Michael.20120322092817.2058: *5* x_2
    def x_2(self, c_init, i):
        while i>30:
            tmp = (c_init&1 ^ c_init&2 ^ c_init&4 ^ c_init&8)%2
            c_init = c_init>>1 ^ tmp*(2**30)
            i -= 1
        return (c_init >> i) & 1

    #@-others
    #@+node:Michael.20120322092817.2059: *4* Sepcial_subframe_Relative
    #@+others
    #@+node:Michael.20120322092817.2060: *5* get_DwPTS_symbol_num
    def get_DwPTS_symbol_num(self):
        DwPTS_symbol_num = (
            (3, 9, 10, 11, 12, 3, 9, 10, 11),
            (3, 8, 9, 10, 3, 8, 9)
        )
        return DwPTS_symbol_num[self.config['CP_DL_type']][self.config['special_subframe_config']]
    #@+node:Michael.20120322092817.2061: *5* get_DwPTS_Ts
    def get_DwPTS_Ts(self):
        DwPTS_Ts = (
            (6592, 19760, 21952, 24144, 26336, 6592, 19760, 21952, 24144),
            (7680, 20480, 23040, 25600, 7680, 20480, 23040)
        )
        return DwPTS_Ts[self.config['CP_DL_type']][self.config['special_subframe_config']]
    #@+node:Michael.20120322092817.2062: *5* get_GAP_Ts
    def get_GAP_Ts(self):
        return 30720-self.get_DwPTS_Ts()-self.get_UpPTS_Ts()
    #@+node:Michael.20120322092817.2063: *5* get_UpPTS_symbol_num
    def get_UpPTS_symbol_num(self):
        UpPTS_symbol_num = (
            (1,1,1,1,1,2,2,2,2),
            (1,1,1,1,2,2,2)
        )
        return UpPTS_symbol_num[self.config['CP_UL_type']][self.config['special_subframe_config']]
    #@+node:Michael.20120322092817.2064: *5* get_UpPTS_Ts
    def get_UpPTS_Ts(self):
        UpPTS_Ts = 0
        if self.config['CP_DL_type'] == 0:
            # normal DL CP
            if self.config['CP_UL_type'] == 0:
                if self.config['special_subframe_config'] in (0,1,2,3,4):
                    UpPTS_Ts = 2192
                elif self.config['special_subframe_config'] in (5,6,7,8):
                    UpPTS_Ts = 4384
            else:
                if self.config['special_subframe_config'] in (0,1,2,3,4):
                    UpPTS_Ts = 2560
                elif self.config['special_subframe_config'] in (5,6,7,8):
                    UpPTS_Ts = 5120
        else:
            # extended DL CP
            if self.config['CP_UL_type'] == 0:
                if self.config['special_subframe_config'] in (0,1,2,3):
                    UpPTS_Ts = 2192
                elif self.config['special_subframe_config'] in (4,5,6):
                    UpPTS_Ts = 4384
            else:
                if self.config['special_subframe_config'] in (0,1,2,3):
                    UpPTS_Ts = 2560
                elif self.config['special_subframe_config'] in (4,5,6):
                    UpPTS_Ts = 5120
        return UpPTS_Ts
    #@-others
    #@+node:Michael.20120322092817.2065: *4* UL_PHY
    #@+others
    #@+node:Michael.20120322092817.2066: *5* PRACH
    def set_PRACH_REs(self):
        brushclr = (self.config['color_brush_PRACH_r'],self.config['color_brush_PRACH_g'],self.config['color_brush_PRACH_b'],self.config['color_brush_PRACH_alpha'])
        for re in self.get_PRACH_REs():
            self.re_lattice[re] = brushclr

    def get_PRACH_REs(self):
        start_time = time()
        #print 'PRACH.get_REs starts'
        REs = []
        n_RA_PRBoffset = self.config['n_RA_PRBoffset']
        PRACH_Configuration_Index = self.config['PRACH_Configuration_Index']
        UL_DL_config = self.config['UL_DL_config']
        prach_resource = self.config['RA_PREAMBLE_MAPPING'][(PRACH_Configuration_Index,UL_DL_config)]
        N_UL_RB = self.config['N_UL_RB']
        #for each four-element tuple
        for (f_RA, t_0_RA, t_1_RA, t_2_RA) in prach_resource:
            frames = list()
            for f in range(self.config['start_SFN'], self.config['start_SFN']+self.config['frame_num']):
                if t_0_RA == 0:
                    frames.append(f)
                elif t_0_RA == 1 and f%2==0:
                    frames.append(f)
                elif t_0_RA == 2 and f%2==1:
                    frames.append(f)
            #print frames

            if self.config['Preamble_Format'] !=4:
                subframe = t_1_RA*5 + self.config['UL_DL_S'][t_1_RA*5:].find('U') + t_2_RA
                if f_RA %2 == 0:
                    n_RA_PRB = n_RA_PRBoffset + 6*floor(f_RA/2.)
                else:
                    n_RA_PRB = N_UL_RB -6 -n_RA_PRBoffset -6*floor(f_RA/2.)
            else:   # format 4
                subframe = t_1_RA*5 + self.config['UL_DL_S'][t_1_RA*5:].find('S')
            
            #print frames,slots,n_RA_PRB

            for frame in frames:
                if self.config['Preamble_Format'] in (0,1,2,3):
                    for l in range(self.config['N_UL_symb']*2): #for PRACH format 0-3, a whole RG pair is allocated
                        for k in range(self.config['N_RB_sc']*6):   # always 6 RBs in frequency domain
                            REs.append( (frame,subframe,l,k+n_RA_PRB*self.config['N_RB_sc']) )
                else: # format 4
                    n_f = frame
                    N_SP = self.config['UL_DL_S'].count('S')
                    if ((n_f%2)*(2-N_SP)+t_1_RA) %2==0:
                        n_RA_PRB = 6*f_RA
                    else:
                        n_RA_PRB = self.config['N_UL_RB'] - 6*(f_RA+1)
                    for l in range(self.config['DwPTS']+1,self.config['DwPTS']+self.config['UpPTS']+1):
                        for k in range(self.config['N_RB_sc']*6):
                            REs.append( (frame,subframe,l,k+n_RA_PRB*self.config['N_RB_sc']) )
        #print REs
        #print 'PRACH.get_REs ends.  ',time()-start_time
        return tuple(REs)

    #@-others

    def set_UL_PHY(self):
        
        self.set_PRACH_REs()
    #@-others
#@+node:Michael.20120322092817.2003: *3* Tools
#@+others
#@+node:Michael.20120322092817.2004: *4* class Point
class Point:
    def __init__(self,x,y):
        self.x, self.y = x,y
    
    def __add__(self, p):
        if type(p) == tuple:
            x,y = p
            return Point(self.x+x,self.y+y)
        else:
            return Point(self.x+p.x,self.y+p.y)
    
    def __sub__(self, p):
        return Point(self.x-p.x,self.y-p.y)

    def __str__(self):
        return "%s, %s" % (self.x,self.y)

Size = Point
#@+node:Michael.20120322092817.2005: *4* class ConfigException
class ConfigException(Exception):
    
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return repr(self.value)
    
    
#@-others
#@-others

from time import time
start_time = time()

def main():
    config = Config().get_config()
    tdlte = TDLTE(config, RELattice(), RESizeLattice())
    image_drawer = ImageDrawer(config, tdlte.re_lattice, tdlte.re_size_lattice)

main()
print "Whole program ended after ", time()-start_time, " sec."
os.system('%s.png'%project_name)
#@-others
#@-leo
