from manim import *
import numpy as np

class EigenvectorAnimation(Scene):
    def construct(self):
        # Define the matrix for transformation
        matrix = np.array([[2, 1], [1, 2]])
        
        # Calculate eigenvalues and eigenvectors
        eigenvalues, eigenvectors = np.linalg.eig(matrix)
        
        # Normalize the eigenvectors for better visualization
        eigenvector1 = eigenvectors[:, 0] / np.linalg.norm(eigenvectors[:, 0]) * 2
        eigenvector2 = eigenvectors[:, 1] / np.linalg.norm(eigenvectors[:, 1]) * 2
        
        # ========== SECTION 1 (0-3s): Introduction and regular vector transformation ==========
        
        # Create coordinate system
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            axis_config={"color": GREY},
            x_length=10,
            y_length=10
        ).scale(0.7)
        
        grid = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            background_line_style={
                "stroke_color": LIGHT_GREY,
                "stroke_width": 0.5,
                "stroke_opacity": 0.5
            }
        ).scale(0.7)
        
        # Create title
        title = Text("Most vectors change direction when transformed by a matrix", font_size=36)
        title.to_edge(UP)
        
        # Create matrix display
        matrix_tex = MathTex(
            "A = \\begin{bmatrix} 2 & 1 \\\\ 1 & 2 \\end{bmatrix}"
        ).scale(0.8)
        matrix_tex.to_corner(UR)
        
        # Create regular vectors (blue)
        vec1 = Arrow(axes.get_origin(), axes.c2p(2, 1), buff=0, color=BLUE)
        vec2 = Arrow(axes.get_origin(), axes.c2p(1, 2), buff=0, color=BLUE)
        vec3 = Arrow(axes.get_origin(), axes.c2p(1, -1), buff=0, color=BLUE)
        
        vec1_label = MathTex("\\vec{v}_1", color=BLUE).next_to(vec1.get_end(), UR, buff=0.1).scale(0.8)
        vec2_label = MathTex("\\vec{v}_2", color=BLUE).next_to(vec2.get_end(), UR, buff=0.1).scale(0.8)
        vec3_label = MathTex("\\vec{v}_3", color=BLUE).next_to(vec3.get_end(), UR, buff=0.1).scale(0.8)
        
        # Transformed vectors
        # Apply matrix transformation to the vectors
        transformed_vec1 = Arrow(
            axes.get_origin(), 
            axes.c2p(*(matrix @ np.array([2, 1]))), 
            buff=0, color=BLUE_D
        )
        transformed_vec2 = Arrow(
            axes.get_origin(), 
            axes.c2p(*(matrix @ np.array([1, 2]))), 
            buff=0, color=BLUE_D
        )
        transformed_vec3 = Arrow(
            axes.get_origin(), 
            axes.c2p(*(matrix @ np.array([1, -1]))), 
            buff=0, color=BLUE_D
        )
        
        # Create dashed lines to show original vectors after transformation
        dashed_vec1 = DashedLine(
            axes.get_origin(), 
            axes.c2p(2, 1), 
            stroke_color=BLUE_E, 
            stroke_opacity=0.5
        )
        dashed_vec2 = DashedLine(
            axes.get_origin(), 
            axes.c2p(1, 2), 
            stroke_color=BLUE_E, 
            stroke_opacity=0.5
        )
        dashed_vec3 = DashedLine(
            axes.get_origin(), 
            axes.c2p(1, -1), 
            stroke_color=BLUE_E, 
            stroke_opacity=0.5
        )
        
        # Begin animations for first section
        self.play(
            FadeIn(grid, run_time=1),
            Create(axes, run_time=1)
        )
        self.wait(0.5)
        
        # Show vectors one by one
        self.play(
            GrowArrow(vec1, run_time=0.8),
            FadeIn(vec1_label, run_time=0.8)
        )
        self.play(
            GrowArrow(vec2, run_time=0.8),
            FadeIn(vec2_label, run_time=0.8)
        )
        self.play(
            GrowArrow(vec3, run_time=0.8),
            FadeIn(vec3_label, run_time=0.8)
        )
        
        # Show title and matrix
        self.play(
            Write(title, run_time=1),
            FadeIn(matrix_tex, run_time=1)
        )
        self.wait(0.5)
        
        # Transform vectors
        self.play(
            ReplacementTransform(vec1, transformed_vec1, run_time=1.5),
            FadeIn(dashed_vec1, run_time=1)
        )
        self.play(
            ReplacementTransform(vec2, transformed_vec2, run_time=1.5),
            FadeIn(dashed_vec2, run_time=1)
        )
        self.play(
            ReplacementTransform(vec3, transformed_vec3, run_time=1.5),
            FadeIn(dashed_vec3, run_time=1)
        )
        self.wait(0.5)
        
        # ========== SECTION 2 (3-6s): Introducing eigenvectors ==========
        
        # Reduce opacity of previous vectors
        faded_vectors = Group(
            transformed_vec1, transformed_vec2, transformed_vec3,
            dashed_vec1, dashed_vec2, dashed_vec3,
            vec1_label, vec2_label, vec3_label
        )
        
        # Create new title
        eigenvector_title = Text("But eigenvectors are special!", font_size=36)
        eigenvector_title.to_edge(UP)
        
        # Create eigenvector (eigenvector1 from calculation)
        eigenvec = Arrow(
            axes.get_origin(), 
            axes.c2p(*eigenvector1), 
            buff=0, 
            color=ORANGE
        )
        eigenvec_label = MathTex("\\vec{v}_4", color=ORANGE).next_to(eigenvec.get_end(), UR, buff=0.1).scale(0.8)
        
        # Calculate transformed eigenvector
        transformed_eigenvec = Arrow(
            axes.get_origin(), 
            axes.c2p(*(matrix @ eigenvector1)), 
            buff=0, 
            color=ORANGE
        )
        
        eigenvector_label = Text("Eigenvector", color=ORANGE, font_size=24)
        eigenvector_arrow = Arrow(
            start=ORIGIN, 
            end=RIGHT, 
            color=ORANGE
        ).scale(0.8)
        
        # Position the label and arrow to point to the eigenvector
        eigenvector_label_group = VGroup(eigenvector_label, eigenvector_arrow)
        eigenvector_label_group.arrange(RIGHT)
        eigenvector_label_group.next_to(eigenvec.get_end(), RIGHT, buff=0.5)
        
        # Highlight effect for eigenvector (pulsing animation)
        highlight = Line(
            axes.get_origin(), 
            axes.c2p(*eigenvector1), 
            color=YELLOW, 
            stroke_width=8
        )
        
        # Begin animations for second section
        self.play(
            FadeOut(title),
            FadeIn(eigenvector_title),
            faded_vectors.animate.set_opacity(0.3),
            run_time=1
        )
        
        # Show eigenvector
        self.play(
            GrowArrow(eigenvec, run_time=1),
            FadeIn(eigenvec_label, run_time=1)
        )
        self.wait(0.5)
        
        # Transform eigenvector (only length changes)
        self.play(
            ReplacementTransform(eigenvec, transformed_eigenvec, run_time=1.5)
        )
        
        # Highlight effect showing direction is preserved
        self.play(
            Create(highlight, run_time=0.5),
            FadeIn(eigenvector_label_group, run_time=1)
        )
        self.play(
            highlight.animate.set_stroke(opacity=0), 
            run_time=0.5
        )
        self.play(
            highlight.animate.set_stroke(opacity=1), 
            run_time=0.5
        )
        self.play(
            highlight.animate.set_stroke(opacity=0), 
            run_time=0.5
        )
        
        self.wait(0.5)
        
        # ========== SECTION 3 (6-9s): Eigenvalue equation ==========
        
        # Create the eigenvalue equation
        eigenvalue_eq = MathTex(
            "A\\vec{v}", "=", "\\lambda\\vec{v}"
        ).scale(1.5)
        eigenvalue_eq.move_to(ORIGIN)
        
        # Expanded equation showing matrix multiplication
        expanded_eq = MathTex(
            "\\begin{bmatrix} 2 & 1 \\\\ 1 & 2 \\end{bmatrix}",
            "\\vec{v}",
            "=",
            "\\lambda",
            "\\vec{v}"
        ).scale(1.2)
        
        # Eigenvalue display
        eigenvalue_text = MathTex(
            "\\lambda = 3", 
            color=YELLOW
        ).scale(1.2)
        eigenvalue_text.next_to(expanded_eq, DOWN, buff=0.5)
        
        # Create scaling visualization
        original_vector_line = Line(
            axes.get_origin(), 
            axes.c2p(*eigenvector1), 
            color=ORANGE
        )
        scaled_vector_line = Line(
            axes.get_origin(), 
            axes.c2p(*(3 * eigenvector1)), 
            color=ORANGE
        )
        
        # Begin animations for third section
        self.play(
            FadeOut(eigenvector_title),
            FadeOut(eigenvector_label_group),
            FadeOut(highlight),
            FadeOut(eigenvec_label),
            faded_vectors.animate.set_opacity(0.1),
            transformed_eigenvec.animate.set_opacity(0.5),
            run_time=1
        )
        
        # Show the eigenvalue equation
        self.play(
            Write(eigenvalue_eq, run_time=1.5)
        )
        self.wait(0.5)
        
        # Expand the equation
        self.play(
            ReplacementTransform(eigenvalue_eq, expanded_eq, run_time=1.5)
        )
        self.wait(0.5)
        
        # Show eigenvalue
        self.play(
            Write(eigenvalue_text, run_time=1),
            eigenvalue_text.animate.set_color(YELLOW),
            run_time=0.8
        )
        self.wait(0.5)
        
        # Demonstrate scaling
        self.play(
            ReplacementTransform(transformed_eigenvec, original_vector_line, run_time=1)
        )
        self.play(
            ReplacementTransform(original_vector_line, scaled_vector_line, run_time=1.5)
        )
        
        self.wait(0.5)
        
        # ========== SECTION 4 (9-12s): Circle transformation and multiple eigenvectors ==========
        
        # Clear previous elements
        self.play(
            FadeOut(expanded_eq),
            FadeOut(eigenvalue_text),
            FadeOut(scaled_vector_line),
            FadeOut(faded_vectors),
            run_time=1
        )
        
        # Create a new title
        natural_directions_title = Text(
            "Eigenvectors reveal the 'natural directions' of a transformation", 
            font_size=32
        ).to_edge(UP)
        
        # Create both eigenvectors
        eigenvec1 = Arrow(
            axes.get_origin(), 
            axes.c2p(*eigenvector1), 
            buff=0, 
            color=ORANGE
        )
        eigenvec2 = Arrow(
            axes.get_origin(), 
            axes.c2p(*eigenvector2), 
            buff=0, 
            color=ORANGE
        )
        
        eigenvec1_label = MathTex("\\vec{v}_1", color=ORANGE).next_to(eigenvec1.get_end(), UR, buff=0.1).scale(0.8)
        eigenvec2_label = MathTex("\\vec{v}_2", color=ORANGE).next_to(eigenvec2.get_end(), UR, buff=0.1).scale(0.8)
        
        # Create circle
        circle = Circle(radius=2, color=BLUE).scale(0.7)
        circle.move_to(axes.get_origin())
        
        # Create ellipse (the transformed circle)
        # The semi-major and semi-minor axes are determined by the eigenvalues
        ellipse = Ellipse(
            width=2 * eigenvalues[0] * 0.7 * 2, 
            height=2 * eigenvalues[1] * 0.7 * 2, 
            color=BLUE_D
        )
        ellipse.move_to(axes.get_origin())
        
        # Begin animations for fourth section
        self.play(
            FadeIn(natural_directions_title, run_time=1)
        )
        
        # Show eigenvectors
        self.play(
            GrowArrow(eigenvec1, run_time=0.8),
            FadeIn(eigenvec1_label, run_time=0.8)
        )
        self.play(
            GrowArrow(eigenvec2, run_time=0.8),
            FadeIn(eigenvec2_label, run_time=0.8)
        )
        
        # Show circle
        self.play(
            Create(circle, run_time=1)
        )
        self.wait(0.5)
        
        # Transform circle to ellipse
        self.play(
            ReplacementTransform(circle, ellipse, run_time=2)
        )
        
        # Highlight eigenvectors as principal axes
        highlight1 = Line(
            axes.c2p(*(-eigenvalues[0] * eigenvector1)), 
            axes.c2p(*(eigenvalues[0] * eigenvector1)), 
            color=YELLOW, 
            stroke_width=3
        )
        highlight2 = Line(
            axes.c2p(*(-eigenvalues[1] * eigenvector2)), 
            axes.c2p(*(eigenvalues[1] * eigenvector2)), 
            color=YELLOW, 
            stroke_width=3
        )
        
        self.play(
            Create(highlight1, run_time=0.8),
            Create(highlight2, run_time=0.8)
        )
        self.wait(0.5)
        
        # ========== SECTION 5 (12-15s): Summary ==========
        
        # Clear previous elements except eigenvectors
        self.play(
            FadeOut(natural_directions_title),
            FadeOut(ellipse),
            FadeOut(highlight1),
            FadeOut(highlight2),
            FadeOut(eigenvec2),
            FadeOut(eigenvec2_label),
            FadeOut(eigenvec1_label),
            run_time=1
        )
        
        # Create summary title
        summary_title = Text("Key Properties of Eigenvectors", font_size=36).to_edge(UP)
        
        # Create key points
        key_point1 = Text("• Eigenvectors maintain their direction", font_size=28, color=WHITE)
        key_point2 = Text("• Eigenvalues show the scaling factor", font_size=28, color=WHITE)
        
        key_points = VGroup(key_point1, key_point2).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        key_points.next_to(summary_title, DOWN, buff=0.5)
        
        # Create final eigenvector with pulsing effect
        final_eigenvec = Arrow(
            axes.get_origin(), 
            axes.c2p(*eigenvector1), 
            buff=0, 
            color=ORANGE
        )
        
        # Begin