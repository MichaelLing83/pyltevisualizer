'''
Created on 23 dec 2013

@author: Michael Duo Ling
'''
from PIL import Image, ImageDraw
from ToolClasses import Point, Size
import Config
from Enums import SF_TYPE, DUPLEX_MODE
from ToolClasses import ReTypeSubframe

class ImageDrawer:
    def __init__(self, duplexMode, reTypeSubframeList):
        '''
        config:    Config module
        reTypeSubframeList: a list of ReTypeSubframe, which marks the usage of each RE in a list of subframes
        '''
        self.reTypeSubframeList = reTypeSubframeList
        self.RB_count = 0
        if (duplexMode == DUPLEX_MODE.FDD):
            dl_start_pos = Config.DrawingConfig.draw_offset
            ul_start_pos = Point(0, 0)
            self.dl_subframe_index, self.ul_subframe_index = 0, 0
            self.initialize_fdd_drawer()
            for dl_subframe in [s for s in self.reTypeSubframeList if s.sfType==SF_TYPE.D]:
                dl_start_pos = self.draw_fdd_subframe(dl_start_pos, self.dl_subframe_size, dl_subframe) + Config.DrawingConfig.subframe_gap
            for ul_subframe in [s for s in self.reTypeSubframeList if s.sfType==SF_TYPE.U]:
                ul_start_pos = self.draw_fdd_subframe(ul_start_pos, self.ul_subframe_size, ul_subframe) + Config.DrawingConfig.subframe_gap
            self.draw('%s.png'%Config.project_name)
        else:
            # TDD
            self.subframe_index = 0
            raise Exception("TDD drawing is not supported yet!")
            self.draw('%s.png'%Config.project_name)

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
    def _draw_mark(self):
        font = self.dc.getfont()
        r, g, b, alpha = 0, 0, 0, 128
        text_width, text_height = font.getsize('A'*len(Config.project_owner))
        pic_width, pic_height = text_width, text_height
        font_color = (0,0,0)
        start_x, start_y = self.config['draw_offset_x']+self.config['image_width']/3*2, self.config['lattice_height']+self.config['draw_offset_y']+(self.config['image_height']-self.config['lattice_height'])/6
        self.dc.text( (start_x, start_y), Config.project_owner, font_color )
        start_y += text_height+5
        self.dc.text( (start_x, start_y), Config.project_weblink, font_color )

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

    def draw(self, file_name):
        #self._draw_lattice()
        #self._draw_REs()
        #self._draw_legend()
        #self._draw_mark()
        self.image.save(file_name)
    
    def draw_fdd_subframe(self, start_pos, size, subframe):
        '''
        Draw one FDD subframe.
        '''
        # initialize pen colors
        penclr = Config.DrawingConfig.color_line_DL_RE
        # draw all vertical lines
        line = (start_pos.x, start_pos.y, start_pos.x, start_pos.y+size.y)
        self.dc.line(line, penclr)
        for l in range(subframe.columnDimension):
            line = (start_pos.x+Config.DrawingConfig.RE_SIZE.x*(l+1), start_pos.y,
                    start_pos.x+Config.DrawingConfig.RE_SIZE.x*(l+1), start_pos.y+size.y)
            self.dc.line(line, penclr)
        # draw all horizontal lines
        line = (start_pos.x, start_pos.y, start_pos.x+size.x, start_pos.y)
        self.dc.line(line, penclr)
        for k in range(subframe.rowDimension):
            line = (start_pos.x, start_pos.y+Config.DrawingConfig.RE_SIZE.y*(k+1),
                    start_pos.x+size.x, start_pos.y+Config.DrawingConfig.RE_SIZE.y*(k+1))
            self.dc.line(line, penclr)
        return start_pos + Size(size.x, 0)

    def initialize_fdd_drawer(self):
        '''
        First we want to calculate how much width we need to plot the whole thing. However, it's a little different for FDD.
        We just make it work here for now, and to make it better later.
        '''
        # calculate DL/UL subframe size
        self.dl_subframe_size = Size(0, 0)
        for subframe in [s for s in self.reTypeSubframeList if s.sfType==SF_TYPE.D]:
            self.dl_subframe_size = Size(subframe.columnDimension * Config.DrawingConfig.RE_SIZE.x,
                                         Config.DrawingConfig.RE_SIZE.y * Config.GlobalConfig.N_DL_RB * Config.GlobalConfig.N_RB_sc)
            break
        self.ul_subframe_size = Size(0, 0)
        for subframe in [s for s in self.reTypeSubframeList if s.sfType==SF_TYPE.U]:
            self.ul_subframe_size = Size(subframe.columnDimension * Config.DrawingConfig.RE_SIZE.x,
                                         Config.DrawingConfig.RE_SIZE.y * Config.GlobalConfig.N_UL_RB * Config.GlobalConfig.N_RB_sc)
            break
        # calculate total drawing size
        dl_width = self.dl_subframe_size.x * len([s for s in self.reTypeSubframeList if s.sfType==SF_TYPE.D])
        ul_width = self.ul_subframe_size.x * len([s for s in self.reTypeSubframeList if s.sfType==SF_TYPE.U])
        total_height = Config.DrawingConfig.RE_SIZE.y * (Config.GlobalConfig.N_DL_RB + Config.GlobalConfig.N_UL_RB) * Config.GlobalConfig.N_RB_sc + Config.DrawingConfig.gap_ul_dl_for_fdd
        # TODO: beautify the plot
        self.lattice_size = Size(max(dl_width, ul_width), total_height)
        self.image_size = self.lattice_size + Config.DrawingConfig.image_margin
        
        self.image = Image.new("RGB", self.image_size.toTuple(), (255,255,255))
        self.dc = ImageDraw.Draw(self.image)

if __name__ == '__main__':
    reTypeSubframeList = list()
    for s in Config.subframeConfigs:
        reTypeSubframeList.append(ReTypeSubframe(Config.GlobalConfig.DownlinkBandwidth, Config.GlobalConfig.DlCyclicPrefixLength, Config.GlobalConfig.DeltaF, SF_TYPE.D, s.longSfn, s.numberOfPdcchSymbols()))
    imageDrawer = ImageDrawer(Config.GlobalConfig.DuplexMode, reTypeSubframeList)