from manim import *
import numpy as np

class VectorAddition(Scene):
    def construct(self):
        plane = NumberPlane(
            x_range=[-5, 5],
            y_range=[-5, 5],
            background_line_style={
                "stroke_opacity": 0.4
            }
        ).add_coordinates()
        
        self.play(Create(plane))
        
        vector_v = Arrow(
            start=ORIGIN,
            end=np.array([2, 2, 0]),
            color=BLUE,
            buff=0
        )
        vector_w = Arrow(
            start=ORIGIN,
            end=np.array([3, 0, 0]),
            color=RED,
            buff=0
        )
        
        v_label = MathTex("\\vec{v}", color=BLUE).next_to(vector_v, UP)
        w_label = MathTex("\\vec{w}", color=RED).next_to(vector_w, UP)
        
        self.play(
            Create(vector_v),
            Write(v_label)
        )
        self.play(
            Create(vector_w),
            Write(w_label)
        )
        
        w_copy = vector_w.copy()
        w_label_copy = w_label.copy()
        
        end_point = vector_v.get_end()
        translated_w = Arrow(
            start=end_point,
            end=end_point + vector_w.get_vector(),
            color=RED,
            buff=0
        )
        
        dashed_line = DashedLine(
            vector_w.get_start(),
            translated_w.get_start(),
            color=GRAY
        )
        
        self.play(
            Create(dashed_line),
            Transform(w_copy, translated_w),
            Transform(w_label_copy, w_label_copy.copy().next_to(translated_w, UP))
        )
        
        resultant = Arrow(
            start=ORIGIN,
            end=translated_w.get_end(),
            color=GREEN,
            buff=0
        )
        
        result_label = MathTex("\\vec{v} + \\vec{w}", color=GREEN).next_to(resultant, UP)
        
        self.play(
            Create(resultant),
            Write(result_label)
        )
        
        equation = MathTex(
            "\\vec{v} + \\vec{w} = \\vec{w} + \\vec{v}"
        ).to_edge(UP)
        
        self.play(Write(equation))
        
        self.play(
            FadeOut(w_copy),
            FadeOut(w_label_copy),
            FadeOut(dashed_line)
        )
        
        new_w = vector_w.copy()
        new_v = vector_v.copy()
        
        self.play(
            new_w.animate.shift(vector_v.get_vector()),
            new_v.animate.shift(vector_w.get_vector())
        )
        
        self.play(
            resultant.animate.set_color(YELLOW),
            Flash(resultant.get_end())
        )
        
        self.play(
            FadeOut(equation),
            FadeOut(new_w),
            FadeOut(new_v),
            resultant.animate.set_color(GREEN)
        )
        
        self.wait()