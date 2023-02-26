from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.graphics.transformation import Matrix

class ZoomApp(App):
    pass

#Code stolen from https://stackoverflow.com/questions/49807052/kivy-scroll-to-zoom
class ScrollableImg(Scatter):
    def on_touch_down(self, touch):
        if touch.is_mouse_scrolling:
            factor = None
            if touch.button == 'scrolldown':
                if self.scale < self.scale_max:
                    factor = 1.1
            elif touch.button == 'scrollup':
                if self.scale > self.scale_min:
                    factor = 1 / 1.1
            if factor is not None:
                #Apply a transformation matrix to the vector [x, y, z, w] representing the image
                #The matrix will make everything appear 'smaller' and 'bigger' depending on factor
                self.apply_transform(Matrix().scale(factor, factor, factor),
                                anchor=touch.pos)
        else:
            super().on_touch_down(touch)

#This implementation does not lock onto the mouse cursor, and is probably a tad worse
class ScrollableImg2(Scatter):
    def on_touch_down(self, touch):
        # Override Scatter's `on_touch_down` behavior for mouse scroll
        if touch.is_mouse_scrolling:
            if touch.button == 'scrolldown':
                if self.scale < 10:
                    self.scale = self.scale * 1.1
            elif touch.button == 'scrollup':
                if self.scale > 1:
                    self.scale = self.scale * 0.8
        # If some other kind of "touch": Fall back on Scatter's behavior
        else:
            super().on_touch_down(touch)


if __name__ == '__main__':
    ZoomApp().run()