from manim import *
import numpy as np

class EigenvalueVisualization(Scene):
    def construct(self):
        # Educational Purpose: Set up coordinate system to establish context
        plane = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_opacity": 0.6
            }
        ).add_coordinates()
        
        # Initial vector setup
        eigen_vector = Vector([2, 1], color=YELLOW)
        regular_vectors = VGroup(*[
            Vector([1, 2], color=BLUE_C),
            Vector([2, -1], color=BLUE_C),
            Vector([-1, 1], color=BLUE_C)
        ])
        
        # Matrix transformation setup
        matrix = [[2, 1], [1, 2]]  # Matrix with eigenvalue 3
        
        # Educational Purpose: Introduce the coordinate system and initial vector
        self.play(
            Create(plane),
            run_time=1.5
        )
        self.play(
            GrowArrow(eigen_vector),
            *[GrowArrow(v) for v in regular_vectors],
            run_time=1.5
        )
        self.wait(0.5)
        
        # Educational Purpose: Show matrix transformation effect
        original_vector_dashed = DashedLine(
            start=ORIGIN,
            end=eigen_vector.get_end(),
            color=YELLOW_D,
            stroke_opacity=0.5
        )
        
        # Transform the plane and vectors
        self.play(
            ApplyMatrix(matrix, plane),
            ApplyMatrix(matrix, regular_vectors),
            ApplyMatrix(matrix, eigen_vector),
            Create(original_vector_dashed),
            run_time=3
        )
        self.wait(0.5)
        
        # Educational Purpose: Emphasize eigenvector behavior
        eigen_glow = eigen_vector.copy().set_stroke(
            color=YELLOW,
            opacity=0.3,
            width=20
        )
        
        self.play(
            FadeIn(eigen_glow),
            eigen_vector.animate.set_stroke(width=6),
            run_time=1
        )
        self.play(
            FadeOut(eigen_glow),
            eigen_vector.animate.set_stroke(width=4),
            run_time=1
        )
        
        # Educational Purpose: Connect to mathematical notation
        eigenvalue_eq = MathTex(
            "\\lambda", "\\vec{v}", "=", "A", "\\vec{v}",
            font_size=36
        )
        eigenvalue_eq.shift(UP * 2)
        lambda_value = MathTex("\\lambda = 3", font_size=36)
        lambda_value.next_to(eigen_vector.get_end(), RIGHT)
        
        self.play(
            Write(eigenvalue_eq),
            Write(lambda_value),
            run_time=2
        )
        self.wait(0.5)
        
        # Educational Purpose: Conclude with key concept
        title = Text(
            "Eigenvalues: The Magic Numbers of Linear Transformations",
            font_size=36
        ).to_edge(UP)
        
        self.play(
            FadeOut(eigenvalue_eq),
            FadeOut(lambda_value),
            FadeOut(eigen_glow),
            ApplyMatrix(np.linalg.inv(matrix), plane),
            ApplyMatrix(np.linalg.inv(matrix), regular_vectors),
            ApplyMatrix(np.linalg.inv(matrix), eigen_vector),
            FadeOut(original_vector_dashed),
            Write(title),
            run_time=3
        )
        self.wait(1)

if __name__ == "__main__":
    scene = EigenvalueVisualization()   
    scene.render()