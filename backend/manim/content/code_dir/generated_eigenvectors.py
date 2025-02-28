from manim import *

class EigenvectorVisualization(Scene):
    def construct(self):
        # Define colors for consistency
        EIGEN_COLOR = GOLD
        REGULAR_COLOR = BLUE
        MATRIX_COLOR = WHITE
        EIGENVALUE_COLOR = RED

        # Create and display coordinate grid
        plane = NumberPlane(
            x_range=[-5, 5],
            y_range=[-5, 5],
            background_line_style={
                "stroke_color": GRAY,
                "stroke_opacity": 0.5
            }
        ).set_opacity(0.5)
        self.play(Create(plane), run_time=1)

        # Create vectors
        eigen_vector = Vector([1, 0.5], color=EIGEN_COLOR)
        regular_vector = Vector([1, 1], color=REGULAR_COLOR)
        
        # Show vectors
        self.play(GrowArrow(eigen_vector), GrowArrow(regular_vector), run_time=1)
        self.wait(0.5)

        # Display transformation matrix
        matrix = MathTex(
            "\\begin{bmatrix} 2 & 1 \\\\ 1 & 2 \\end{bmatrix}",
            color=MATRIX_COLOR
        ).to_corner(UR)
        self.play(Write(matrix), run_time=1)
        self.wait(0.5)

        # Create dashed line along eigenvector
        dashed_line = DashedLine(
            start=ORIGIN,
            end=3 * eigen_vector.get_end(),
            color=EIGEN_COLOR,
            opacity=0.5
        )

        # Apply transformation
        matrix_transform = [[2, 1], [1, 2]]
        self.play(
            Create(dashed_line),
            ApplyMatrix(matrix_transform, eigen_vector),
            ApplyMatrix(matrix_transform, regular_vector),
            run_time=3
        )
        self.wait(1)

        # Show eigenvalue
        eigenvalue_label = MathTex("\\lambda = 3", color=EIGENVALUE_COLOR)
        eigenvalue_label.next_to(eigen_vector.get_end(), UR)
        self.play(Write(eigenvalue_label), run_time=1)

        # Add "Same Direction!" annotation with circular arrow
        direction_text = Text("Same Direction!", color=EIGEN_COLOR, font_size=24)
        direction_text.next_to(eigen_vector.get_end(), RIGHT)
        
        arc = Arc(
            radius=0.5,
            angle=-TAU/4,
            color=EIGEN_COLOR
        ).next_to(direction_text, LEFT)
        
        self.play(
            Write(direction_text),
            Create(arc),
            run_time=1
        )

        # Show equation Av = λv
        equation = MathTex(
            "A", "v", "=", "\\lambda", "v",
            tex_to_color_map={
                "A": MATRIX_COLOR,
                "v": EIGEN_COLOR,
                "\\lambda": EIGENVALUE_COLOR
            }
        ).to_edge(DOWN)

        # Reveal equation components
        self.play(Write(equation), run_time=1)
        self.wait(0.5)

        # Create connecting lines
        matrix_line = DashedLine(
            matrix.get_center(),
            equation[0].get_center(),
            color=MATRIX_COLOR,
            dash_length=0.1
        )
        vector_line = DashedLine(
            eigen_vector.get_center(),
            equation[1].get_center(),
            color=EIGEN_COLOR,
            dash_length=0.1
        )
        
        self.play(
            Create(matrix_line),
            Create(vector_line),
            run_time=2
        )

        # Final highlighting of eigenvector
        self.play(
            Flash(
                eigen_vector.get_end(),
                color=EIGEN_COLOR,
                flash_radius=0.5
            ),
            run_time=1
        )
        
        # Hold final state
        self.wait(3)
        
if __name__ == "__main__":
    scene = EigenvectorVisualization()   
    scene.render()