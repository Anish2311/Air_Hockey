import py5

class Puck:
    def __init__(self,x,y):
        self.pos = py5.Py5Vector2D(x,y)
        self.vel = py5.Py5Vector2D(10,10)
        self.acc = py5.Py5Vector2D(0,0)
        self.rad = 25

    def show(self):
        py5.fill(255)
        py5.no_stroke()
        py5.circle(self.pos.x,self.pos.y,2*self.rad)

    def update(self):
        self.acc = -0.007*self.vel 
        self.vel += self.acc
        mag = min(40,self.vel.mag)
        self.vel.normalize()
        self.vel *= mag
        self.pos += self.vel

        if self.pos.y - self.rad < 0:
            self.pos.y = self.rad
            self.vel.y *= -1
        if self.pos.y + self.rad > py5.height:
            self.pos.y = py5.height - self.rad
            self.vel.y *= -1
        if self.pos.x - self.rad < 0:
            self.pos.x = self.rad
            self.vel.x *= -1
        if self.pos.x + self.rad > py5.width:
            self.pos.x = py5.width - self.rad
            self.vel.x *= -1

class Player:
    def __init__(self,x,y):
        self.pos = py5.Py5Vector2D(x,y)
        self.vel = py5.Py5Vector2D(0,0)
        self.rad = 50

    def show(self):
        py5.fill(255)
        py5.no_stroke()
        py5.circle(self.pos.x,self.pos.y,self.rad*2)

    def update(self):
        self.pos += self.vel

        if (self.pos.x - puck.pos.x)**2 + (self.pos.y - puck.pos.y)**2 < (puck.rad + self.rad)**2:
            force = py5.Py5Vector2D.__sub__(py5.Py5Vector2D(self.pos.x,self.pos.y),puck.pos)
            force.normalize()
    
            puck.pos -= force*(-py5.sqrt((self.pos.x - puck.pos.x)**2 + (self.pos.y - puck.pos.y)**2) + (puck.rad + self.rad))
    
            rel_force = self.vel
            rel_vel = py5.Py5Vector2D.__sub__(puck.vel,rel_force)
            mag = -2*rel_vel.mag*py5.cos(py5.Py5Vector2D.angle_between(force,rel_vel))
            force *= mag
    
            # print(force,(py5.Py5Vector2D.angle_between(force,puck.vel)))
    
            puck.vel += force

    def move(self,m):

        self.vel = m

def setup():
    global puck
    global player_1
    global player_2

    py5.size(1400, 800)
    py5.rect_mode(py5.CENTER)
    puck = Puck(py5.width/2,py5.height/2)
    player_1 = Player(py5.width - py5.width/10,py5.height/2)
    player_2 = Player(py5.width/10,py5.height/2)

def draw():
    py5.background(0)

    puck.update()
    puck.show()

    player_1_mov = py5.Py5Vector2D.__sub__(player_1.pos,py5.Py5Vector2D(py5.mouse_x,py5.mouse_y))
    mag = min(50,player_1_mov.mag)
    player_1_mov.normalize()
    player_1_mov.mag *= -mag

    player_2_mov = py5.Py5Vector2D.__sub__(player_2.pos,py5.Py5Vector2D((py5.width/2)*py5.noise((py5.frame_count/100)),py5.height*py5.noise(((py5.frame_count + 100000)/100))))
    mag = min(50,player_2_mov.mag)
    player_2_mov.normalize()
    player_2_mov.mag *= -mag

    player_1.move(player_1_mov)
    player_1.update()
    player_1.show()

    player_2.move(player_2_mov)
    player_2.update()
    player_2.show()

if __name__ == "__main__":
    py5.run_sketch()
    puck = None
    player_1 = None
    player_2 = None
    drag_array = [(0,0),(0,0)]