'''
Created on 20 dec 2013

@author: linggduo

Terminology:
    1. longSf: long subframe number, which is systemFrameNumber * 10 + subframeNumber
'''
project_version = '2.0.0'
project_name = 'pyLTEVisualizer'
project_owner = "Author: Michael Duo Ling, Email: duo.ling.cn@gmail.com"
project_weblink = "http://code.google.com/p/pyltevisualizer/"

from PIL import Image, ImageDraw


ENUM_MAX = 0

class RE_TYPE:
    '''
    Resource Element Type: used to mark each RE which PHY signal/channel is using this one.
    '''
    global ENUM_MAX
    size = 9
    AVAILABLE, CSRS_PORT0, CSRS_PORT1, CSRS_PORT2, CSRS_PORT3, CSRS_PORT4, CSRS_PORT5, CSRS_PORT6, CSRS_PORT7 = range(ENUM_MAX, ENUM_MAX+size)
    ENUM_MAX += size

class SF_TYPE:
    '''
    enum class for subframe type
    '''
    global ENUM_MAX
    size = 3
    D, U, S = range(ENUM_MAX, ENUM_MAX+size)
    ENUM_MAX += size

class CP_TYPE:
    '''
    Cyclic Prefix Type
    '''
    global ENUM_MAX
    size = 2
    NORMAL, EXTENDED = range(ENUM_MAX, ENUM_MAX+size)
    ENUM_MAX += size

class DELTA_F:
    '''
    delta_f, 15 kHz or 7.5 kHz.
    '''
    global ENUM_MAX
    size = 2
    KHZ_7_5, KHZ_15 = range(ENUM_MAX, ENUM_MAX+size)
    ENUM_MAX += size

class BW:
    '''
    Up-link or down-link BandWidth
    '''
    global ENUM_MAX
    size = 6
    N6, N15, N25, N50, N75, N100 = range(ENUM_MAX, ENUM_MAX+size)
    ENUM_MAX += size
    @staticmethod
    def toReNumber(bw, cpType, delta_f):
        '''
        Calculate number of sub-carriers for the whole bandwidth.
        '''
        return BW.toRbNumber(bw) * BW.calc__N_RB_sc(cpType, delta_f)
    @staticmethod
    def toRbNumber(bw):
        '''
        Calculate number of Resource Blocks from given band-width.
        '''
        return (6,15,25,50,75,100)[bw-BW.N6]
    @staticmethod
    def calc__N_RB_sc(cpType, delta_f):
        '''
        Calculate number of sub-carriers for one Resource Block, according to table 6.2.3-1 in 36.211.
        '''
        if delta_f == DELTA_F.KHZ_15:
            return 12
        elif delta_f == DELTA_F.KHZ_7_5:
            return 24
        raise Exception("Unknown delta_f={0}".format(delta_f))

class ReTypeMatrix:
    '''
    Represents a matrix of Resource Elements. It's fast to grab any column of this matrix, but not rows.
    '''
    def __init__(self, rowDimension, columnDimension):
        self.rowDimension = rowDimension
        self.columnDimension = columnDimension
        self.m = [[RE_TYPE.AVAILABLE for j in range(self.rowDimension)] for i in range(self.columnDimension)]
    def getColumn(self, columnIndex):
        return self.m[columnIndex]

class ReTypeSubframe(ReTypeMatrix):
    '''
    Represents a subframe.
    '''
    def __init__(self, bw, cpType, delta_f, sfType, longSf, numOfPdcchSymbols):
        self.bw = bw
        self.cpType = cpType
        self.numOfPdcchSymbols = numOfPdcchSymbols
        self.sfType = sfType
        self.longSf = longSf
        super.__init(self, BW.toReNumber(bw, cpType, delta_f), 2*ReTypeSubframe.calcOfdmSymbolNumPerSlot(cpType, delta_f))
    @staticmethod
    def calcOfdmSymbolNumPerSlot(cpType, delta_f):
        '''
        Calculate number of OFDM symbols per slot.
        '''
        if cpType==CP_TYPE.NORMAL:
            return 7
        elif cpType==CP_TYPE.EXTENDED:
            if delta_f==DELTA_F.KHZ_15:
                return 6
            elif delta_f==DELTA_F.KHZ_7_5:
                return 3
        raise Exception("Unknown combination: cpType={0}, delta_f={1}".format(cpType, delta_f))

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
                    if (frame,subframe,l,0) in self.re_size_lattice:
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
                    if (frame,subframe,l,0) in self.re_size_lattice:
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
            else:    # 'S'
                length = self.config['special_RB_width']
            self.dc.text( (x+0.5*length,y), str(i), penclr )
            x += length
    #@+node:Michael.20120322092817.1931: *4* draw
    def draw(self, file_name):
        #start_time = time()
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
                    if (frame,subframe,l,0) in self.re_size_lattice:
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
        

if __name__ == '__main__':
    pass