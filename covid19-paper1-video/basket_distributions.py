import numpy as np
from manimlib.animation.creation import ShowCreation, Write
from manimlib.animation.fading import FadeOut, FadeIn, FadeOutAndShift
from manimlib.animation.growing import GrowFromCenter, GrowArrow
from manimlib.animation.transform import Transform, ApplyMethod
from manimlib.constants import DOWN, UP, RIGHT, LEFT, ORIGIN, FRAME_WIDTH, FRAME_X_RADIUS, UR, BOTTOM, LEFT_SIDE
from manimlib.mobject.geometry import Rectangle, Arrow
from manimlib.mobject.number_line import NumberLine
from manimlib.mobject.svg.brace import Brace
from manimlib.mobject.svg.tex_mobject import TextMobject
from manimlib.mobject.types.vectorized_mobject import VGroup
from manimlib.scene.scene import Scene
from pygments.styles import paraiso_light


class BasketDistributions(Scene):
  _apple_count: int = 10
  _banana_count: int = 6
  _apple_fraction: float = _apple_count / (_apple_count + _banana_count)
  _banana_fraction: float = _banana_count / (_apple_count + _banana_count)
  _apple_colour = paraiso_light.RED
  _banana_colour = paraiso_light.YELLOW

  def _main_title(self):
    paper_name_a = TextMobject("Simulating human interactions in supermarkets to")
    paper_name_b = TextMobject("measure the risk of COVID-19 contagion at scale")
    author_list_a = TextMobject("Serge Plata\\quad Sumanas Sarma\\quad Melvin Lancelot")
    author_list_b = TextMobject("Kristine Bagrova\\quad David Romano-Critchley")
    arxiv = TextMobject("arXiv:2006.15213")

    paper_name_a.shift(UP)
    paper_name_b.next_to(paper_name_a, DOWN)

    author_list_a.scale(0.8)
    author_list_b.scale(0.8)

    author_list_a.next_to(paper_name_b, DOWN + DOWN)
    author_list_b.next_to(author_list_a, DOWN)

    arxiv.scale(0.6)
    arxiv.next_to(author_list_b, DOWN + DOWN)

    self.play(FadeIn(paper_name_a), FadeIn(paper_name_b))
    self.wait()
    self.play(FadeIn(author_list_a), FadeIn(author_list_b))
    self.play(FadeIn(arxiv))

    self.wait(4)
    self.play(FadeOut(paper_name_a),
              FadeOut(paper_name_b),
              FadeOut(author_list_a),
              FadeOut(author_list_b),
              ApplyMethod(arxiv.move_to, BOTTOM + (UP * 0.5)))

  def construct(self):
    self._main_title()

    text_one = TextMobject("Given a list of items sold")
    text_two: TextMobject = TextMobject("Randomly choose items matching this distribution")
    text_two.next_to(text_one, DOWN)
    number_line = NumberLine(numbers_with_elongated_ticks=[0, 1],
                             include_numbers=True,
                             x_min=0,
                             x_max=1,
                             unit_size=10,
                             tick_frequency=0.1,
                             # decimal_number_config={"num_decimal_places": 1},
                             numbers_to_show=[0, 1])
    number_line.next_to(text_two, UP)

    self.play(ShowCreation(text_one))
    self.wait()
    self.play(ShowCreation(text_two))
    self.wait(4)

    apples_text = TextMobject("Apples:")
    apples_text.set_color(self._apple_colour)

    apples_text.to_edge(UP)
    apples_text.align_to(text_two, LEFT)

    apple_count_text = TextMobject(f"{self._apple_count}")
    apple_count_text.set_color(self._apple_colour)
    apple_count_text.next_to(apples_text, RIGHT)

    banana_text = TextMobject("Bananas:")
    banana_text.set_color(self._banana_colour)

    banana_text.next_to(apples_text, DOWN)
    banana_text.align_to(apples_text, LEFT)

    banana_count_text = TextMobject(f"{self._banana_count}")
    banana_count_text.set_color(self._banana_colour)
    banana_count_text.next_to(banana_text, RIGHT)

    self.play(Transform(text_one, apples_text))
    self.play(ShowCreation(apple_count_text))
    self.play(ShowCreation(banana_text), ShowCreation(banana_count_text))

    banana_bar = Rectangle(height=0.4,
                           width=number_line.point_to_number(self._banana_fraction * 10) * (
                             number_line.number_to_point(1)[0]),
                           color=self._banana_colour,
                           fill_color=self._banana_colour,
                           fill_opacity=0.75)
    banana_bar.next_to(banana_count_text, RIGHT + RIGHT)

    apple_bar = Rectangle(height=0.4,
                          width=number_line.point_to_number(self._apple_fraction * 10) * (
                            number_line.number_to_point(1)[0]),
                          color=self._apple_colour,
                          fill_color=self._apple_colour,
                          fill_opacity=0.75)
    apple_bar.next_to(banana_bar, UP)
    apple_bar.align_to(banana_bar, LEFT)

    self.play(FadeIn(apple_bar), FadeIn(banana_bar))

    self.wait(1.5)

    apple_fraction_text = TextMobject(
      "$\\frac{" + str(self._apple_count) + "}{" + str(self._apple_count + self._banana_count) + "} = " + str(
        self._apple_fraction) + "$")
    apple_fraction_text.next_to(apple_bar, RIGHT)

    banana_fraction_text = TextMobject(
      "$\\frac{" + str(self._banana_count) + "}{" + str(self._apple_count + self._banana_count) + "} = " + str(
        self._banana_fraction) + "$")
    banana_fraction_text.next_to(banana_bar, RIGHT)

    self.play(ShowCreation(apple_fraction_text))
    self.play(ShowCreation(banana_fraction_text))

    self.wait(2)

    number_line_map_text = TextMobject("Map these counts to values between 0 and 1")
    number_line_map_text.next_to(text_two, UP)
    self.play(ShowCreation(number_line_map_text))

    self.wait(3)
    self.play(Transform(number_line_map_text, number_line))

    apple_num_ln_bar = Rectangle(height=0.4,
                                 # width=1 - self._apple_fraction * (number_line.number_to_point(1)[0]),
                                 width=number_line.point_to_number(self._apple_fraction * 10) * (
                                   number_line.number_to_point(1)[0]),
                                 color=self._apple_colour,
                                 fill_color=self._apple_colour,
                                 fill_opacity=0.25)
    apple_num_ln_bar.move_to(apple_bar, LEFT)
    self.add(apple_num_ln_bar)
    self.wait(2)
    self.play(ApplyMethod(apple_num_ln_bar.move_to,
                          number_line.number_to_point(0),
                          LEFT))

    banana_num_ln_bar = Rectangle(height=0.4,
                                  width=number_line.point_to_number(self._banana_fraction * 10) * (
                                    number_line.number_to_point(1)[0]),
                                  color=self._banana_colour,
                                  fill_color=self._banana_colour,
                                  fill_opacity=0.25)
    banana_num_ln_bar.move_to(banana_bar, LEFT)
    self.add(banana_num_ln_bar)
    self.wait(2)
    self.play(ApplyMethod(banana_num_ln_bar.move_to,
                          number_line.number_to_point(1),
                          RIGHT))

    text_scale: float = 0.75
    get_rnd_full = TextMobject("Get a random number $n$ between 0 and 1 (uniform distribution)")

    get_apple_text = TextMobject(f"Apple\\quad if $n <= {self._apple_fraction}$",
                                 tex_to_color_map={"Apple": self._apple_colour})
    get_banana_text = TextMobject(f"Banana\\quad if $n > {self._apple_fraction}$",
                                  tex_to_color_map={"Banana": self._banana_colour})

    get_rnd_full.scale(text_scale)
    get_rnd_full.next_to(text_two, DOWN)
    get_banana_text.next_to(get_apple_text, DOWN)
    step_group = VGroup(get_apple_text, get_banana_text)

    brace = Brace(step_group, LEFT)
    step_text_d = brace.get_text("$n \\sim U(0, 1)$")
    step_text_d.scale(text_scale)
    step_text_d.next_to(get_rnd_full, DOWN + DOWN)
    step_text_d.shift(LEFT)
    brace.next_to(step_text_d, RIGHT)

    step_group.scale(text_scale)
    step_group.next_to(step_text_d, RIGHT + RIGHT + RIGHT)

    self.wait(2)
    self.play(ShowCreation(get_rnd_full))
    self.wait(2)
    self.play(ShowCreation(step_text_d))
    self.wait(2)

    self.play(GrowFromCenter(brace))
    self.wait()
    self.play(ShowCreation(get_apple_text))
    self.wait(2)
    self.play(ShowCreation(get_banana_text))

    # random_nos_to_draw = 10
    # main_arrow = Arrow(ORIGIN, DOWN * 1.3)
    # helper_arrow = Arrow(ORIGIN, LEFT * 1.3)
    #
    # for i in range(random_nos_to_draw):
    #   num: float = np.random.random_sample(1)
    #   point = number_line.number_to_point(num)
    #   arrow_colour = self._apple_colour if num <= self._apple_fraction else self._banana_colour
    #   arrow_recipient = get_apple_text if num <= self._apple_fraction else get_banana_text
    #
    #   main_arrow.set_color(arrow_colour)
    #
    #   if i == 0:
    #     main_arrow.next_to(point, UP)
    #     helper_arrow.next_to(arrow_recipient, RIGHT)
    #     self.play(GrowArrow(main_arrow), GrowArrow(helper_arrow))
    #   else:
    #     self.play(ApplyMethod(helper_arrow.next_to, arrow_recipient, RIGHT),
    #               ApplyMethod(main_arrow.next_to, point, UP))
    #   self.wait()
    #
    # self.play(FadeOut(main_arrow), FadeOut(helper_arrow))
    self.wait()
