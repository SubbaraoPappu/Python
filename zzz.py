class Planet:
    def revolve(self):
        print('revolve')
    def rotate(self):
        print('rotate')
    def rev_rot(self):
        self.revolve()
        self.rotate()


earth=Planet()
# earth.revolve()
# earth.rotate()

earth.rev_rot()



