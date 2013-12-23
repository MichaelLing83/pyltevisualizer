'''
Created on 23 dec 2013

@author: Michael Duo Ling
'''
from PIL import Image, ImageDraw
import Config
from Enums import SF_TYPE

class Point:
    def __init__(self,x,y):
        self.x, self.y = x, y
    
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
    
    def x(self):
        return self.x
    
    def y(self):
        return self.y

Size = Point

class ImageDrawer:
    def __init__(self, config, reTypeSubframeList):
        '''
        config:    Config module
        reTypeSubframeList: a list of ReTypeSubframe, which marks the usage of each RE in a list of subframes
        '''
        self.config = config
        self.reTypeSubframeList = reTypeSubframeList
        self.initialize_drawer()
        self.RB_count = 0
        self.draw('%s.png'%Config.project_name)

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
        self._draw_lattice()
        self._draw_REs()
        self._draw_legend()
        self._draw_mark()
        self.image.save(file_name)

    def initialize_drawer_fdd(self):
        dl_width = 0
        for subframe in self.reTypeSubframeList if subframe.subframeType==SF_TYPE.D:
            
        for subframe in self.reTypeSubframeList:    # for each subframe in the list
            width += subframe.columnDimension * Config.DrawingConfig.RE_SIZE.x()
            width += 1
        self.lattice_width = width
        self.lattice_height = Config.DrawingConfig.RE_SIZE.y() * self.config['N_DL_RB']*12
        self.config['image_width'] = self.config['lattice_width'] + 30
        self.config['image_height'] = self.config['lattice_height'] + 70
        
        self.image = Image.new("RGB",(self.config['image_width'],self.config['image_height']),(255,255,255))
        self.dc = ImageDraw.Draw(self.image)