from manim import *

class RecursionAnimation(Scene):
    def construct(self):
        # Define color scheme
        COLOR_MAP = {
            "title": BLUE,
            "code": WHITE,
            "highlight": GREEN,
            "base_case": RED,
            "function_call": BLUE_B,
            "arrow": YELLOW,
            "output": WHITE,
            "caption": YELLOW
        }
        
        # Title section: Introduce the concept of recursion (0-3s)
        title = Text("Recursion", color=COLOR_MAP["title"], font_size=72)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))
        
        # Display the recursive countdown function
        code_text = '''def countDown(n):
    if n == 0:  # Base case
        return
    else:       # Recursive case
        print(n)
        countDown(n-1)'''
        
        code = Code(
            code=code_text,
            tab_width=4,
            background="rectangle",
            language="Python",
            font="Monospace",
            font_size=24
        )
        
        self.play(Create(code))
        self.wait(1.5)
        
        # Transition code to upper left corner (3-6s)
        code_small = code.copy().scale(0.6).to_corner(UL, buff=0.5)
        self.play(Transform(code, code_small))
        
        # Create the first function call
        initial_call_text = Text("countDown(5)", font_size=36, color=COLOR_MAP["function_call"])
        initial_call_box = SurroundingRectangle(initial_call_text, buff=0.3, color=COLOR_MAP["function_call"])
        initial_call_group = VGroup(initial_call_text, initial_call_box).move_to(ORIGIN)
        
        self.play(
            FadeIn(initial_call_group)
        )
        self.wait(0.5)
        
        # Highlight the print statement in the first call
        printed_value = Text("5", font_size=32, color=COLOR_MAP["highlight"])
        printed_value.next_to(initial_call_group, DOWN, buff=0.3)
        printed_box = SurroundingRectangle(printed_value, buff=0.1, color=COLOR_MAP["highlight"])
        
        self.play(
            FadeIn(printed_value),
            Create(printed_box)
        )
        self.wait(0.5)
        self.play(FadeOut(printed_box))
        
        # Recursion winding phase: Create nested function calls (6-9s)
        # We'll create boxes for countDown(4) through countDown(0)
        call_boxes = {5: initial_call_group}
        printed_values = {5: printed_value}
        arrows = {}
        
        # Function to create a new call box and arrow
        def create_call(n, prev_n):
            call_text = Text(f"countDown({n})", font_size=36 - (5-n)*3, color=COLOR_MAP["function_call"])
            
            # Determine color based on whether it's base case or recursive
            if n == 0:
                box_color = COLOR_MAP["base_case"]  # Red for base case
            else:
                # Gradually darken blue for deeper recursion
                opacity = 0.5 + (n / 10)
                box_color = Color(rgb=BLUE_B.get_rgb()) * opacity
            
            call_box = SurroundingRectangle(call_text, buff=0.3, color=box_color)
            call_group = VGroup(call_text, call_box)
            
            # Position boxes in a stair-like pattern
            prev_box = call_boxes[prev_n]
            call_group.next_to(prev_box, DR, buff=0.7)
            
            # Create arrow connecting the boxes
            arrow = Arrow(
                prev_box.get_bottom() + DOWN * 0.2,
                call_group.get_top() + UP * 0.2,
                buff=0.2,
                color=COLOR_MAP["arrow"]
            )
            
            return call_group, arrow
        
        # Create recursive calls from countDown(4) to countDown(0)
        for n in range(4, -1, -1):
            call_group, arrow = create_call(n, n+1)
            call_boxes[n] = call_group
            arrows[n+1] = arrow
            
            self.play(
                GrowArrow(arrow),
                FadeIn(call_group),
                run_time=0.7
            )
            
            # For non-base cases, show the print operation
            if n > 0:
                printed_val = Text(str(n), font_size=32 - (5-n)*3, color=COLOR_MAP["highlight"])
                printed_val.next_to(call_group, DOWN, buff=0.3)
                printed_box = SurroundingRectangle(printed_val, buff=0.1, color=COLOR_MAP["highlight"])
                
                self.play(
                    FadeIn(printed_val),
                    Create(printed_box)
                )
                self.wait(0.3)
                self.play(FadeOut(printed_box))
                
                printed_values[n] = printed_val
            else:
                # For base case, show a checkmark to indicate return without printing
                checkmark = Text("✓", font_size=30, color=GREEN)
                checkmark.next_to(call_group, RIGHT, buff=0.3)
                self.play(FadeIn(checkmark))
                self.wait(0.5)
                
        self.wait(1)  # Pause at the base case
        
        # Recursion unwinding phase: Complete function calls in reverse (9-12s)
        for n in range(0, 6):
            if n in call_boxes:
                # Fade out the function call
                self.play(
                    FadeOut(call_boxes[n]),
                    run_time=0.5
                )
                
                # Also fade out the arrow that pointed to this call
                if n+1 in arrows:
                    self.play(FadeOut(arrows[n+1]), run_time=0.3)
        
        # Show the output at the bottom (12-15s)
        output_text = Text("Output: 5, 4, 3, 2, 1", font_size=36, color=COLOR_MAP["output"])
        output_text.to_edge(DOWN, buff=1.5)
        
        self.play(FadeIn(output_text))
        self.wait(1)
        
        # Show closing caption
        caption = Text(
            "Recursion: Solving problems by breaking them\ninto smaller versions of the same problem.",
            font_size=32,
            color=COLOR_MAP["caption"]
        )
        caption.next_to(output_text, UP, buff=0.8)
        
        self.play(Write(caption))
        self.wait(3)
        
        # Fade out everything for clean ending
        self.play(
            FadeOut(code),
            FadeOut(output_text),
            FadeOut(caption),
            *[FadeOut(val) for val in printed_values.values()]
        )
        self.wait(1)

if __name__ == "__main__":
    scene = RecursionAnimation()
    scene.render()