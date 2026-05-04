from gamelib import *

game = Game(1200,1000,"Roguelite")

def positionObjects( objects ):
    for i in range(len(objects)):
        x = randint(100,900)
        y = randint(100, 700)
        objects[i].moveTo(x, y)
        objects[i].visible = True


skeleton = []
for i in range(5):
    s = Animation("./images/skeletonwalk.png",13,game, 286/13,33, 6)
    s.resizeBy(100)
    skeleton.append(s)
positionObjects(skeleton)

def hero_control():
    hero.draw()
    hero1.draw()
    heroatk.draw()
    healthbar.moveTo( 44, 925 )
    healthbar.width = hero.health*11.1
    if keys.Pressed[K_w]:
        hero.visible=False
        hero1.visible=True
        hero1.y -= 7
        heroatk.flipV=False
    if keys.Pressed[K_w] and keys.Pressed[K_q]:
        hero.visible=False
        hero1.visible=True
        hero1.y -= 17
        heroatk.flipV=False
    if keys.Pressed[K_s]:
        hero.visible=False
        hero1.visible=True
        hero1.y += 7
        heroatk.flipV=False
    if keys.Pressed[K_s] and keys.Pressed[K_q]:
        hero.visible=False
        hero1.visible=True
        hero1.y += 17
        heroatk.flipV=False
    if keys.Pressed[K_d]:
        hero.visible=False
        hero1.visible=True
        hero1.x += 7
        hero.flipV = False
        heroatk.flipV=False
    if keys.Pressed[K_d] and keys.Pressed[K_q]:
        hero.visible=False
        hero1.visible=True
        hero1.x += 17
        hero.flipV = False
        heroatk.flipV=False
    if keys.Pressed[K_a]:
        hero1.flipV = True
        hero.flipV=True
        heroatk.flipV=True
        hero.visible=False
        hero1.visible=True
        hero1.x -= 7
    else:
        hero1.flipV=False
    if keys.Pressed[K_a] and keys.Pressed[K_q]:
        hero1.flipV = True
        hero.flipV=True
        heroatk.flipV=True
        hero.visible=False
        hero1.visible=True
        hero1.x -= 17

    arrow.move()
    warrow.move()
    sarrow.move()
    darrow.move()

    
    if arrow.x < 0 or arrow.x > 1200:
        arrow.visible = False
    if darrow.x < 0 or darrow.x > 1200:
        darrow.visible = False
    if warrow.y < 0 or warrow.y > 1200:
        warrow.visible = False
    if sarrow.y < 0 or sarrow.y > 1200:
        sarrow.visible = False
        
    if keys.Pressed[K_a] and keys.Pressed[K_e] and arrow.visible==False:
        arrow.moveTo(hero1.x, hero1.y+30)
        arrow.visible=True
        arrow.setSpeed(10,90)

    if keys.Pressed[K_d] and keys.Pressed[K_e] and darrow.visible==False:
        darrow.moveTo(hero1.x, hero1.y+30)
        darrow.setSpeed(10,-90)
        darrow.visible=True
        darrow.flipV = False

    if keys.Pressed[K_w] and keys.Pressed[K_e] and warrow.visible==False:
        warrow.moveTo(hero1.x, hero1.y)
        warrow.setSpeed(10,0)
        warrow.visible=True
        warrow.flipV=False

    if keys.Pressed[K_s] and keys.Pressed[K_e] and sarrow.visible==False:
        sarrow.moveTo(hero1.x, hero1.y+40)
        sarrow.setSpeed(10,180)
        sarrow.visible=True

        
    if keys.Pressed[K_SPACE] and not keys.Pressed[K_a] and not keys.Pressed[K_w] and not keys.Pressed[K_d] and not keys.Pressed[K_s]:
        heroatk.visible=True
        heroatk.moveTo(heroatk.x, heroatk.y)
        hero.moveTo(heroatk.x, heroatk.y)
        hero1.moveTo(heroatk.x, heroatk.y)
        hero.visible=False
        hero1.setImage(heroatk.image)
        hero.setImage(heroatk.image)
        hero1.visible=False
    else:
        heroatk.visible=False

    if not keys.Pressed[K_SPACE] and not keys.Pressed[K_a] and not keys.Pressed[K_w] and not keys.Pressed[K_d] and not keys.Pressed[K_s]:
        hero.visible=True
        hero1.visible=False
        hero.moveTo(hero1.x, hero1.y)
        heroatk.moveTo(hero.x, hero.y)
        heroatk.moveTo(hero1.x, hero1.y)


bg = Image("map.jpg",game)
bg.resizeTo(1200, 1000)
bg.draw()

hero= Animation("./images/_Idle.png",10, game, 1200/10, 80,20)
hero.resizeBy(100)
hero1= Animation("./images/_Run.png",10, game, 1200/10, 80,5)
hero1.resizeBy(100)
hero2= Animation("./images/_Run2.png",10, game, 1200/10, 80,5)
hero2.resizeBy(100)
heroatk=Animation("./images/_Attack2.png", 6, game, 720/6, 80, 15)
heroatk.resizeBy(100)
skeletonatk = Animation("./images/skeletonatk.png",11,game, 774/18,37, 15)
skeletonatk.resizeBy(100)
bossatk=Animation("./images/atk.jpg", 4, game, 626/4, 192, 15)
bossatk.resizeBy(100)
bosswalk=Animation("./images/walk.jpg", 6, game, 920/6, 179, 15)
bosswalk.resizeBy(100)
arrow=Image("./images/arrow.png", game)
arrow.resizeBy(-70)
sarrow=Image("./images/sarrow.png", game)
sarrow.resizeBy(-70)
darrow=Image("./images/darrow.png", game)
darrow.resizeBy(-70)
warrow=Image("./images/warrow.png", game)
warrow.resizeBy(-70)

healthbar = Shape("bar",game, hero.health, 25, red)
warrow.visible=False
arrow.visible=False
sarrow.visible=False
darrow.visible=False

skeletonbars = []
for s in skeleton:
    bar = Shape("bar", game, s.health, 15, red)
    skeletonbars.append(bar)



for s in skeleton:
    s.health = 3000

title = Image("./images/title.png",game)
title.y = 200
play = Image("./images/play.png",game)
play.y = +700
f=Font(red, 40, black, "Comic Sans MS")
hit = Sound("./sounds/hit.mp3", 1)
pain = Sound("./sounds/pain.mp3", 2)
swing = Sound("./sounds/swing.mp3", 3)
while not game.over:
    game.processInput()
    play.draw()
    title.draw()

    if keys.Pressed[K_SPACE]:
        game.over = True

    game.drawText("Press [Space] to start", 1200, game.height -1000 ,f)
    game.update(30)

game.over = False


while not game.over:
    game.processInput()
    bg.draw()
    hero_control()
    
    for i in range(len(skeleton)):
        s = skeleton[i]
        bar = skeletonbars[i]

        d = math.sqrt((hero.x - s.x)**2 + (hero.y - s.y)**2)

        if d < 42:
            s.moveTowards(hero1, 0)
            skeletonatk.visible = True
        else:
            s.moveTowards(hero1, 2)
            skeletonatk.visible = False

        s.draw()

        bar.moveTo(s.x - 34, s.y + 30)
        bar.width = s.health / 60
        bar.draw()

        if heroatk.collidedWith(s):
            s.health -= 50

        if s.collidedWith(hero):
            hero.health -= 0.1

        if s.collidedWith(heroatk):
            hero.health -= 0.1

        if s.collidedWith(hero1):
            hero.health -= 0.1

        if s.health <= 0 and s.visible:
            s.visible = False
            s.moveTo(99999, 99999)
            game.score += 10

        if arrow.collidedWith(skeletonatk):
            skeletonatk.health -= 150

        if arrow.collidedWith(s):
            s.health -= 150

        if warrow.collidedWith(skeletonatk):
            skeletonatk.health -= 150

        if warrow.collidedWith(s):
            s.health -= 150

        if sarrow.collidedWith(skeletonatk):
            skeletonatk.health -= 150

        if sarrow.collidedWith(s):
            s.health -= 150

        if darrow.collidedWith(skeletonatk):
            skeletonatk.health -= 150

        if darrow.collidedWith(s):
            s.health -= 150


    if hero.health <= 0 or game.score == 50:
        game.over = True
    
    game.update(60)

bosswalk.health=134000

game.over=False

while not game.over and hero.health>0:
    game.processInput()
    bg.draw()
    hero_control()
    bosswalk.draw()
    bossatk.draw()

    d1 = math.sqrt((hero.x - bosswalk.x)**2 + (hero.y - bosswalk.y)**2)

    bar.moveTo(bosswalk.x - 60, bosswalk.y + 90)
    bar.width = bosswalk.health / 804
    bar.draw()

    if d1 < 42:
        bosswalk.moveTowards(hero1, 0)
        bossatk.visible = True
        bosswalk.visible=False
        bossatk.visible=True
        bossatk.moveTo(bosswalk.x, bosswalk.y)
    else:
        bosswalk.moveTowards(hero1, 2)
        bossatk.visible = False
        bosswalk.visible=True

    if bossatk.collidedWith(hero):
        hero.health -= 0.35

    if bossatk.collidedWith(heroatk):
        hero.health -= 0.15

    if bossatk.collidedWith(hero1):
        hero.health -= 0.01

    if heroatk.collidedWith(bosswalk):
        bosswalk.health -= 150

    if heroatk.collidedWith(bossatk):
        bosswalk.health -= 150

    if arrow.collidedWith(bosswalk):
        bosswalk.health -= 150

    if arrow.collidedWith(bossatk):
        bosswalk.health -= 150

    if warrow.collidedWith(bosswalk):
        bosswalk.health -= 150

    if warrow.collidedWith(bossatk):
        bosswalk.health -= 150

    if sarrow.collidedWith(bosswalk):
        bosswalk.health -= 150

    if sarrow.collidedWith(bossatk):
        bosswalk.health -= 150

    if darrow.collidedWith(bosswalk):
        bosswalk.health -= 150

    if darrow.collidedWith(bossatk):
        bosswalk.health -= 150

    if bosswalk.health<0:
        game.over=True

    game.update(60)
end = Image("./images/end.png",game)
end.y = +700
end.resizeTo(700,700)
bg = Image("pink.png",game)
bg.resizeTo(1200, 1000)
bg.draw()

while not game.over:
    game.processInput()
    end.draw()
    title.draw()

    if keys.Pressed[K_SPACE]:
        game.over = True

    game.drawText("Press [Space] to end", 1200, game.height -1000 ,f)
    game.update(30)


    game.update(60)
game.quit()
