import pygame
import libardrone
import time

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    drone = libardrone.ARDrone()
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYUP:
                drone.hover()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    drone.reset()
                    running = False
                # takeoff / land
                elif event.key == pygame.K_RETURN:
                    drone.takeoff()
                    drone.speed = 0.7
                elif event.key == pygame.K_SPACE:
                    drone.land()
                # emergency
                elif event.key == pygame.K_BACKSPACE:
                    drone.reset()
                # forward / backward
                elif event.key == pygame.K_w:
                    drone.move_forward()
                elif event.key == pygame.K_s:
                    drone.move_backward()
                # left / right
                elif event.key == pygame.K_a:
                    drone.move_left()
                elif event.key == pygame.K_d:
                    drone.move_right()
                # up / down
                elif event.key == pygame.K_UP:
                    drone.move_up()
                elif event.key == pygame.K_DOWN:
                    drone.move_down()
                # turn left / turn right
                elif event.key == pygame.K_LEFT:
                    drone.turn_left()
                elif event.key == pygame.K_RIGHT:
                    drone.turn_right()
                # speed
                elif event.key == pygame.K_1:
                    drone.speed = 0.1
                elif event.key == pygame.K_2:
                    drone.speed = 0.2
                elif event.key == pygame.K_3:
                    drone.speed = 0.3
                elif event.key == pygame.K_4:
                    drone.speed = 0.4
                elif event.key == pygame.K_5:
                    drone.speed = 0.5
                elif event.key == pygame.K_6:
                    drone.speed = 0.6
                elif event.key == pygame.K_7:
                    drone.speed = 0.7
                elif event.key == pygame.K_8:
                    drone.speed = 0.8
                elif event.key == pygame.K_9:
                    drone.speed = 0.9
                elif event.key == pygame.K_0:
                    drone.speed = 1.0


        try:
            pass#surface = pygame.image.fromstring(drone.image, (W, H), 'RGB')
        except:
            print("werkt niet 1")

        #drone.network_process.run()

        try:
            # battery status
            hud_color =  (255, 0, 0) if drone.navdata.get('drone_state', dict()).get('emergency_mask', 1) else (10, 10, 255)
            bat = drone.navdata.get(0, dict()).get('battery', 0)
            fly = drone.navdata.get(0, dict()).get('fly_mask', 0)
            alt = drone.navdata.get(0, dict()).get('altitude', 0)
            vx = drone.navdata.get(0, dict()).get('vx', 0)
            vy = drone.navdata.get(0, dict()).get('vy', 0)
            vz = drone.navdata.get(0, dict()).get('vz', 0)
            theta = drone.navdata.get(0, dict()).get('theta', 0)
            phi = drone.navdata.get(0, dict()).get('phi', 0)
            psi = drone.navdata.get(0, dict()).get('psi', 0)

            f = pygame.font.Font(None, 20)
            hud = f.render('Battery: %i%%' % bat, True, hud_color)
            hud2 = f.render('fly state: %i%%' % fly, True, hud_color)
            hud3 = f.render('altitude: %i%% mm' % alt, True, hud_color)
            hud4 = f.render('vx: %i%%' % vx, True, hud_color)
            hud5 = f.render('vy: %i%%' % vy, True, hud_color)
            hud6 = f.render('vz: %i%%' % vz, True, hud_color)
            hud7 = f.render('theta: %i%%' % theta, True, hud_color)
            hud8 = f.render('phi: %i%%' % phi, True, hud_color)
            hud9 = f.render('psi: %i%%' % psi, True, hud_color)
            print(drone.navdata.get('drone_state', dict()))
        except:
            print("werkt niet 2")
        try:
            #screen.blit(surface, (0, 0))
            screen.fill((0,0,0))
            screen.blit(hud, (10, 10))
            screen.blit(hud2, (10, 50))
            screen.blit(hud3, (10, 100))
            screen.blit(hud4, (10, 150))
            screen.blit(hud5, (10, 200))
            screen.blit(hud6, (10, 250))
            screen.blit(hud7, (200, 150))
            screen.blit(hud8, (200, 200))
            screen.blit(hud9, (200, 250))

        except:
            print("werkt niet 3")


        pygame.display.flip()
        clock.tick(50)
        pygame.display.set_caption("FPS: %.2f" % clock.get_fps())

    print "Shutting down...",
    drone.halt()
    print "Ok."

if __name__ == '__main__':
    main()
