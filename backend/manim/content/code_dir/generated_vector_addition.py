from manim import *

class VectorAdditionScene(Scene):
    def construct(self):
        # Set the stage with a coordinate plane
        axes = Axes(
            x_range=[-3, 5],
            y_range=[-3, 5],
            axis_config={"color": GREY},
            x_length=6,
            y_length=6
        ).add_coordinates()
        
        # Create our vectors
        vector_a = Vector([2, 1], color=BLUE)
        vector_b = Vector([1, 2], color=RED)
        
        # Labels for vectors
        label_a = MathTex("A", color=BLUE).next_to(vector_a.get_center(), DOWN+RIGHT, buff=0.1).scale(0.8)
        label_b = MathTex("B", color=RED).next_to(vector_b.get_center(), UP+LEFT, buff=0.1).scale(0.8)
        
        # Initial setup - show coordinate plane
        self.play(FadeIn(axes), run_time=1)
        self.wait(0.5)
        
        # Show the initial vectors at the origin
        self.play(
            Create(vector_a),
            Create(vector_b),
            run_time=1
        )
        self.play(
            Write(label_a),
            Write(label_b),
            run_time=0.5
        )
        self.wait(0.5)
        
        # --- Head-to-Tail Method ---
        # Create a copy of vector B to move to the head of vector A
        vector_b_copy = vector_b.copy()
        
        # Save original positioning of labels for later
        original_a_pos = label_a.get_center()
        original_b_pos = label_b.get_center()
        
        # Move vector B to the head of vector A (Head-to-Tail method)
        # Calculate the end point of vector A to position B
        end_point_a = vector_a.get_end()
        
        # Create an animation path for the movement of vector B
        def update_vector_b_copy(mob, alpha):
            # Start from origin (0,0,0) and move to end_point_a
            new_start = np.array([0, 0, 0]) * (1 - alpha) + end_point_a * alpha
            new_vector = Vector([1, 2], color=RED).shift(new_start)
            mob.become(new_vector)
            return mob
        
        # Move the label B with vector B
        self.play(
            UpdateFromAlphaFunc(vector_b_copy, update_vector_b_copy),
            label_b.animate.next_to(vector_b_copy.get_end() + end_point_a, UP+LEFT, buff=0.1),
            run_time=1.5
        )
        self.wait(0.5)
        
        # Create the resultant vector C (A+B) as a dashed line
        resultant_c = DashedLine(
            start=ORIGIN,
            end=vector_b_copy.get_end() + end_point_a,
            color=PURPLE_B,
            stroke_width=5,
            dash_length=0.15
        )
        
        # Create solid resultant vector for better visibility
        resultant_vec = Vector(
            direction=vector_b_copy.get_end() + end_point_a,
            color=PURPLE_B
        )
        
        # Label for resultant vector
        label_c = MathTex("A+B", color=PURPLE_B).next_to(resultant_c.get_center(), RIGHT, buff=0.1).scale(0.8)
        
        # Show the resultant vector
        self.play(
            Create(resultant_c),
            Create(resultant_vec),
            Write(label_c),
            run_time=1
        )
        self.wait(1)
        
        # Reset and prepare for parallelogram method
        self.play(
            FadeOut(vector_b_copy),
            FadeOut(resultant_c),
            FadeOut(resultant_vec),
            FadeOut(label_c),
            Transform(label_b, MathTex("B", color=RED).next_to(vector_b.get_center(), UP+LEFT, buff=0.1).scale(0.8)),
            run_time=1
        )
        
        # --- Parallelogram Method ---
        # Create copies of vectors for the parallelogram
        vector_a_copy = vector_a.copy().set_opacity(0.5)
        vector_b_copy = vector_b.copy().set_opacity(0.5)
        
        # Shift the copies to form a parallelogram
        vector_a_copy.shift(vector_b.get_end())
        vector_b_copy.shift(vector_a.get_end())
        
        # Create dotted lines for the parallelogram
        dotted_line1 = DashedLine(
            vector_a.get_end(),
            vector_a.get_end() + vector_b.get_end(),
            color=GREY,
            stroke_opacity=0.8,
            stroke_width=2
        )
        
        dotted_line2 = DashedLine(
            vector_b.get_end(),
            vector_a.get_end() + vector_b.get_end(),
            color=GREY,
            stroke_opacity=0.8,
            stroke_width=2
        )
        
        # Show the parallelogram construction
        self.play(
            Create(vector_a_copy),
            Create(vector_b_copy),
            run_time=1
        )
        self.play(
            Create(dotted_line1),
            Create(dotted_line2),
            run_time=1
        )
        self.wait(0.5)
        
        # Highlight the diagonal as the resultant vector
        resultant_para = Vector(
            direction=vector_a.get_end() + vector_b.get_end(),
            color=PURPLE_B
        )
        
        label_result_para = MathTex("A+B", color=PURPLE_B).next_to(resultant_para.get_center(), DOWN+RIGHT, buff=0.15).scale(0.8)
        
        self.play(
            Create(resultant_para),
            Write(label_result_para),
            run_time=1
        )
        self.wait(1)
        
        # Clean up for commutativity demonstration
        self.play(
            FadeOut(vector_a_copy),
            FadeOut(vector_b_copy),
            FadeOut(dotted_line1),
            FadeOut(dotted_line2),
            FadeOut(resultant_para),
            FadeOut(label_result_para),
            run_time=1
        )
        
        # --- Commutativity Demonstration ---
        # Create a new copy of vector A to move to the head of vector B
        vector_a_copy = vector_a.copy()
        
        # Move vector A to the head of vector B (showing B+A)
        end_point_b = vector_b.get_end()
        
        def update_vector_a_copy(mob, alpha):
            new_start = np.array([0, 0, 0]) * (1 - alpha) + end_point_b * alpha
            new_vector = Vector([2, 1], color=BLUE).shift(new_start)
            mob.become(new_vector)
            return mob
        
        # Move the label A with vector A
        self.play(
            UpdateFromAlphaFunc(vector_a_copy, update_vector_a_copy),
            label_a.animate.next_to(vector_a_copy.get_end() + end_point_b, DOWN+RIGHT, buff=0.1),
            run_time=1.5
        )
        self.wait(0.5)
        
        # Create the resultant vector (B+A) - should be the same as (A+B)
        resultant_ba = Vector(
            direction=vector_a_copy.get_end() + end_point_b,
            color=PURPLE_B
        )
        
        label_ba = MathTex("B+A", color=PURPLE_B).next_to(resultant_ba.get_center(), RIGHT, buff=0.1).scale(0.8)
        
        self.play(
            Create(resultant_ba),
            Write(label_ba),
            run_time=1
        )
        self.wait(1)
        
        # --- Force Application Demonstration ---
        # Clean up for force application
        self.play(
            FadeOut(vector_a),
            FadeOut(vector_b),
            FadeOut(vector_a_copy),
            FadeOut(resultant_ba),
            FadeOut(label_a),
            FadeOut(label_b),
            FadeOut(label_ba),
            run_time=1
        )
        
        # Create a small circle to represent an object
        object_circle = Circle(radius=0.2, color=WHITE, fill_opacity=0.5).move_to(ORIGIN)
        
        # Create force vectors
        force1 = Vector([2, 1], color=BLUE)
        force2 = Vector([1, 2], color=RED)
        
        # Labels for forces
        label_f1 = MathTex("F_1", color=BLUE).next_to(force1.get_center(), DOWN+RIGHT, buff=0.1).scale(0.8)
        label_f2 = MathTex("F_2", color=RED).next_to(force2.get_center(), UP+LEFT, buff=0.1).scale(0.8)
        
        # Create the net force vector
        net_force = Vector(
            direction=[3, 3],
            color=PURPLE_B
        )
        
        label_net = MathTex("F_{net}", color=PURPLE_B).next_to(net_force.get_center(), RIGHT, buff=0.1).scale(0.8)
        
        # Show the object and forces
        self.play(
            FadeIn(object_circle),
            run_time=0.5
        )
        self.play(
            Create(force1),
            Create(force2),
            Write(label_f1),
            Write(label_f2),
            run_time=1
        )
        self.play(
            Create(net_force),
            Write(label_net),
            run_time=1
        )
        self.wait(0.5)
        
        # Final summary text
        summary = Text("Vector Addition: A + B = B + A", color=YELLOW).scale(0.8).to_edge(DOWN, buff=0.5)
        
        self.play(
            Write(summary),
            run_time=1
        )
        self.wait(1)

if __name__ == "__main__":
    scene = VectorAdditionScene()
    scene.render()