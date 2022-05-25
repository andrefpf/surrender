import numpy as np 

from SurRender import constants


class Tool:
    def __init__(self, viewport):
        self.viewport = viewport
        self.override_viewport_functions()

    def override_viewport_functions(self):
        self.viewport.mousePressEvent = self.mousePressEvent
        self.viewport.mouseMoveEvent = self.mouseMoveEvent
        self.viewport.wheelEvent = self.wheelEvent

    def mousePressEvent(self, event):
        pass
    
    def mouseLeaveEvent(self, event):
        pass 

    def mouseMoveEvent(self, event):
        pass 
    
    def wheelEvent(self, event):
        pass 


class MoveTool(Tool):
    def __init__(self, viewport):
        super().__init__(viewport)

    def mousePressEvent(self, event):
        self.start_pos = event.pos()
    
    def mouseMoveEvent(self, event):
        delta = self.start_pos - event.pos() 
        self.start_pos = event.pos()
        self.viewport.move_xy(delta.x(), -delta.y())
        
    def wheelEvent(self,event):
        x = event.angleDelta().y() / 120
        if x > 0:
            self.viewport.zoom_in(constants.ZOOM_FACTOR)
        elif x < 0:
            self.viewport.zoom_out(constants.ZOOM_FACTOR)


class ZoomTool(Tool):
    def __init__(self, viewport):
        super().__init__(viewport)

    def mousePressEvent(self, event):
        self.start_pos = event.pos()
    
    def mouseMoveEvent(self, event):
        k = 0.1
        delta = self.start_pos - event.pos() 
        factor = 1 + delta.x() * k
        self.start_pos = event.pos()
        self.viewport.zoom_out(factor)
        
    def wheelEvent(self,event):
        x = event.angleDelta().y() / 120
        if x > 0:
            self.viewport.zoom_in(constants.ZOOM_FACTOR)
        elif x < 0:
            self.viewport.zoom_out(constants.ZOOM_FACTOR)