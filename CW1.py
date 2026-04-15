def setup():
     size(400, 400)
     text_align( CENTER,  CENTER)

def draw():
     background(245, 245, 240)

     cx, cy =  width / 2,  height / 2
     R = 160

     now_s =  second()
     now_m =  minute()
     now_h =  hour()

     sec_angle =  remap(now_s, 0, 60, 0,  TWO_PI) -  HALF_PI
     min_angle =  remap(now_m + now_s / 60, 0, 60, 0,  TWO_PI) -  HALF_PI
     hr_angle  =  remap((now_h % 12) + now_m / 60, 0, 12, 0,  TWO_PI) -  HALF_PI
 
     no_stroke()
     fill(160)
     circle(cx, cy, (R + 14) * 2)

     fill(245, 245, 240)
     circle(cx, cy, (R + 8) * 2)

     stroke_cap(ROUND)
     no_stroke()
     fill(60)
     text_size(16)
     for i in range(1, 13):
         a =  remap(i, 0, 12, 0,  TWO_PI) -  HALF_PI
         nr = R - 34
         text(str(i), cx +  cos(a) * nr, cy +  sin(a) * nr)

     def draw_hand(angle, length, tail, weight, col):
         stroke(*col)
         stroke_weight(weight)
         stroke_cap( ROUND)
         line(
            cx -  cos(angle) * tail, cy -  sin(angle) * tail,
            cx +  cos(angle) * length, cy +  sin(angle) * length
         )

     draw_hand(hr_angle,  R * 0.52, 14, 6,   (30, 30, 30))
     draw_hand(min_angle, R * 0.78, 18, 3.5, (70, 70, 70))
     draw_hand(sec_angle, R * 0.88, 22, 1.5, (220, 0, 60))

     no_stroke()
     fill(220, 0, 60)
     circle(cx, cy, 12)
     fill(30)
     circle(cx, cy, 5)
