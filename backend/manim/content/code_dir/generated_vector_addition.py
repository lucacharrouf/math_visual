from manim import *
import numpy as np

class VectorAddition(Scene):
    def construct(self):
        # Set up coordinate plane
        plane = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            x_length=8,
            y_length=6,
            background_line_style={
                "stroke_opacity": 0.6
            }
        ).add_coordinates()
        
        # Create vectors
        vec_a = Arrow(
            plane.coords_to_point(0, 0),
            plane.coords_to_point(2, 1),
            buff=0,
            color=BLUE
        )
        vec_b = Arrow(
            plane.coords_to_point(0, 0),
            plane.coords_to_point(-1, 2),
            buff=0,
            color=RED
        )
        
        # Create labels
        label_a = MathTex("\\vec{a}", color=BLUE).next_to(vec_a, UP+RIGHT, buff=0.1)
        label_b = MathTex("\\vec{b}", color=RED).next_to(vec_b, UP+LEFT, buff=0.1)
        
        # Calculate resultant vector
        end_point = np.array([2-1, 1+2, 0])  # a + b
        vec_c = Arrow(
            plane.coords_to_point(0, 0),
            plane.coords_to_point(end_point[0], end_point[1]),
            buff=0,
            color=PURPLE
        )
        label_c = MathTex("\\vec{c}", color=PURPLE).next_to(vec_c, UP, buff=0.1)
        
        # Create equation
        equation = MathTex(
            "\\vec{a} + \\vec{b} = \\vec{c}",
            color=WHITE
        ).to_edge(UP)
        
        # Initial animations (0-3s)
        self.play(Create(plane))
        self.play(Create(vec_a), Write(label_a))
        self.wait()
        
        # Add second vector (3-6s)
        self.play(Create(vec_b), Write(label_b))
        self.wait()
        
        # Parallel translation (6-9s)
        translated_b = Arrow(
            plane.coords_to_point(2, 1),
            plane.coords_to_point(1, 3),
            buff=0,
            color=RED
        )
        dashed_line = DashedLine(
            vec_b.get_end(),
            translated_b.get_start(),
            color=RED_A
        )
        
        self.play(
            Create(dashed_line),
            Transform(vec_b.copy(), translated_b),
            label_b.animate.next_to(translated_b, UP+LEFT, buff=0.1)
        )
        self.wait()
        
        # Show resultant (9-12s)
        self.play(
            Create(vec_c),
            Write(label_c),
            Write(equation)
        )
        self.wait()
        
        # Show parallelogram (12-15s)
        parallelogram = VGroup(
            Line(vec_a.get_end(), translated_b.get_end(), color=GRAY),
            Line(ORIGIN, vec_a.get_end(), color=GRAY),
            Line(ORIGIN, vec_b.get_end(), color=GRAY),
            Line(vec_b.get_end(), translated_b.get_end(), color=GRAY)
        )
        
        self.play(Create(parallelogram), run_time=0.5)
        self.wait()
        self.play(
            FadeOut(parallelogram),
            FadeOut(dashed_line)
        )
        
        # Final pause
        self.wait(2)
if __name__ == "__main__":
    scene = VectorAddition()   
    scene.render()