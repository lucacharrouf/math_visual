from manim import *

class VectorAdditionScene(Scene):
    def construct(self):
        # Setup the coordinate system
        # Using a relatively small scale to ensure vectors fit nicely on screen
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            axis_config={"color": GREY},
            x_length=7,
            y_length=7
        ).add_coordinates()
        
        # Create a title for the animation
        title = Text("Vector Addition", font_size=48).to_edge(UP, buff=0.5)
        
        # Define our vectors - Vector A (red, northeast) and Vector B (blue, southeast)
        vector_a = Vector([2, 3], color=RED)
        vector_b = Vector([3, -2], color=BLUE)
        
        # Label the vectors
        label_a = MathTex("\\vec{A}", color=RED).next_to(vector_a, UP + RIGHT, buff=0.1)
        label_b = MathTex("\\vec{B}", color=BLUE).next_to(vector_b, DOWN + RIGHT, buff=0.1)
        
        # Section 1: Introduction of coordinate system and vectors
        # Educational purpose: Establish the visual framework for vector operations
        self.play(Create(axes), run_time=1)
        self.wait(0.5)
        
        # Create vectors with GrowArrow for a more dynamic appearance
        self.play(
            GrowArrow(vector_a),
            GrowArrow(vector_b),
            run_time=1
        )
        self.play(
            Write(label_a),
            Write(label_b),
            run_time=0.5
        )
        
        # Show the title
        self.play(Write(title), run_time=1)
        self.wait(1)
        
        # Save original positions for later reference
        vector_b_original = vector_b.copy()
        label_b_original = label_b.copy()
        
        # Section 2: Tip-to-tail method
        # Educational purpose: Demonstrate the sequential addition of vectors
        method_text = Text("Tip-to-tail method", font_size=36).to_edge(UP, buff=0.5)
        
        # Create a faded copy of vector B to leave at origin
        vector_b_ghost = vector_b.copy().set_stroke(opacity=0.3)
        label_b_ghost = label_b.copy().set_opacity(0.3)
        
        # Move vector B to the tip of vector A
        tip_of_a = vector_a.get_end()
        vector_b_moved = vector_b.copy().shift(tip_of_a)
        label_b_moved = label_b.copy().next_to(vector_b_moved, DOWN + RIGHT, buff=0.1)
        
        # Animate the transformation
        self.play(FadeOut(title), run_time=0.5)
        self.play(
            Transform(vector_b, vector_b_moved),
            Transform(label_b, label_b_moved),
            FadeIn(vector_b_ghost),
            FadeIn(label_b_ghost),
            run_time=2
        )
        
        self.play(Write(method_text), run_time=1)
        self.wait(1)
        
        # Section 3: Create the resultant vector C
        # Educational purpose: Show how vectors A and B combine to form resultant C
        vector_c = Vector([2 + 3, 3 + (-2)], color=PURPLE)  # A + B = [5, 1]
        label_c = MathTex("\\vec{C}", color=PURPLE).next_to(vector_c, RIGHT, buff=0.1)
        
        # Highlight effect on the resultant vector
        self.play(GrowArrow(vector_c), run_time=1.5)
        self.play(
            Flash(vector_c.get_end(), color=PURPLE, line_length=0.5, flash_radius=0.5),
            Write(label_c),
            run_time=0.5
        )
        
        # Display the equation
        equation = MathTex("\\vec{A} + \\vec{B} = \\vec{C}", color=WHITE)
        equation.set_color_by_tex("\\vec{A}", RED)
        equation.set_color_by_tex("\\vec{B}", BLUE)
        equation.set_color_by_tex("\\vec{C}", PURPLE)
        equation.to_edge(RIGHT, buff=1).shift(UP)
        
        self.play(Write(equation), run_time=1)
        self.wait(1)
        
        # Section 4: Parallelogram method
        # Educational purpose: Show an alternative but equivalent approach to vector addition
        paralelogram_title = Text("Parallelogram method", font_size=36).to_edge(UP, buff=0.5)
        
        # Move vector B back to origin for parallelogram method
        self.play(
            FadeOut(method_text),
            FadeOut(vector_b_ghost),
            FadeOut(label_b_ghost),
            Transform(vector_b, vector_b_original),
            Transform(label_b, label_b_original),
            run_time=1.5
        )
        
        # Create dashed lines to complete the parallelogram
        dashed_line1 = DashedLine(
            vector_a.get_end(),
            vector_a.get_end() + vector_b.get_end(),
            color=BLUE_D,
            stroke_opacity=0.7
        )
        dashed_line2 = DashedLine(
            vector_b.get_end(),
            vector_a.get_end() + vector_b.get_end(),
            color=RED_D,
            stroke_opacity=0.7
        )
        
        self.play(
            Write(paralelogram_title),
            Create(dashed_line1),
            Create(dashed_line2),
            run_time=1.5
        )
        
        # Highlight the diagonal (resultant vector)
        self.play(
            Indicate(vector_c),
            Flash(vector_c.get_end(), color=PURPLE, line_length=0.5, flash_radius=0.5),
            run_time=1
        )
        self.wait(0.5)
        
        # Section 5: Real-world example - Boat crossing a river
        # Educational purpose: Connect abstract math to practical applications
        real_world_title = Text("Real-world application: River crossing", font_size=36).to_edge(UP, buff=0.5)
        
        # Prepare to clear current elements
        current_mobjects = [
            axes, vector_a, vector_b, vector_c, 
            label_a, label_b, label_c, equation,
            paralelogram_title, dashed_line1, dashed_line2
        ]
        
        # Fade out current elements
        self.play(
            *[FadeOut(mob) for mob in current_mobjects],
            run_time=1
        )
        
        # Create a new coordinate system for the river example
        river_axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            axis_config={"color": GREY},
            x_length=7,
            y_length=7
        )
        
        # Create the river banks
        river_left = Line([-4, -4, 0], [-4, 4, 0], color=BLUE_C, stroke_width=20)
        river_right = Line([4, -4, 0], [4, 4, 0], color=BLUE_C, stroke_width=20)
        water = Rectangle(height=8, width=8, fill_color=BLUE, fill_opacity=0.2).move_to([0, 0, 0])
        
        # Create boat as a simple triangle
        boat = Triangle(fill_color=GREY, fill_opacity=1).scale(0.3).rotate(-PI/2)
        
        # Position at starting point
        boat.move_to([-3, -3, 0])
        
        # Create vectors for the boat example
        boat_motor = Vector([0, 4], color=RED).shift([-3, -3, 0])  # Direction boat wants to go (straight up)
        current = Vector([4, 0], color=BLUE).shift([-3, -3, 0])    # Direction of river current (right)
        actual_path = Vector([4, 4], color=PURPLE).shift([-3, -3, 0])  # Resultant path
        
        # Labels for the boat example
        motor_label = MathTex("\\text{Motor}", color=RED).next_to(boat_motor, LEFT, buff=0.5)
        current_label = MathTex("\\text{Current}", color=BLUE).next_to(current, DOWN, buff=0.5)
        resultant_label = MathTex("\\text{Actual Path}", color=PURPLE).next_to(actual_path, RIGHT, buff=0.5)
        
        # Show the river scene
        self.play(
            FadeIn(river_axes),
            FadeIn(water),
            Create(river_left),
            Create(river_right),
            Write(real_world_title),
            run_time=1
        )
        
        self.play(FadeIn(boat), run_time=0.5)
        
        # Show the vectors one by one
        self.play(GrowArrow(boat_motor), Write(motor_label), run_time=1)
        self.play(GrowArrow(current), Write(current_label), run_time=1)
        
        # Show the resultant path
        self.play(
            GrowArrow(actual_path),
            Write(resultant_label),
            run_time=1
        )
        
        # Animate the boat moving along the resultant path
        boat_path = Line([-3, -3, 0], [1, 1, 0], color=WHITE, stroke_opacity=0)
        self.play(
            MoveAlongPath(boat, boat_path),
            run_time=2
        )
        
        # Final equation to reinforce the concept
        final_equation = MathTex(
            "\\vec{\\text{Motor}} + \\vec{\\text{Current}} = \\vec{\\text{Actual Path}}",
            color=WHITE
        )
        final_equation.set_color_by_tex("\\vec{\\text{Motor}}", RED)
        final_equation.set_color_by_tex("\\vec{\\text{Current}}", BLUE)
        final_equation.set_color_by_tex("\\vec{\\text{Actual Path}}", PURPLE)
        final_equation.to_edge(DOWN, buff=1)
        
        self.play(Write(final_equation), run_time=1)
        
        # Add a conclusion
        conclusion = Text("Vector addition combines both magnitude and direction!", 
                          font_size=24).next_to(final_equation, DOWN, buff=0.5)
        
        self.play(Write(conclusion), run_time=1)
        self.wait(2)

if __name__ == "__main__":
    scene = VectorAdditionScene()
    scene.render()