import anthropic
from prompts import (CONCEPT_BREAKDOWN, ANIMATION_TESTING, DESIGN, 
                   CODE_GENERATION, FEEDBACK_INTEGRATION, 
                   extract_code_only, extract_section)

class ManimGenerator:
    def __init__(self, api_key=None):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = "claude-3-7-sonnet-20250219"
    
    def _send_prompt(self, prompt, max_tokens=3000):
        """Helper method to send a prompt to the API and get the text response"""
        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=max_tokens,
                messages=[{
                    "role": "user",
                    "content": prompt
                }]
            )
            
            # Get the text content from the response
            content_text = ""
            for content_block in message.content:
                if content_block.type == "text":
                    content_text += content_block.text
            
            return content_text
        except Exception as e:
            print(f"Error sending prompt: {e}")
            return None
    
    def analyze_concept(self, math_topic, audience_level="high school"):
        """Break down a mathematical concept for visualization"""
        formatted_prompt = CONCEPT_BREAKDOWN.format(
            topic=math_topic,
            audience_level=audience_level
        )
        response = self._send_prompt(formatted_prompt, max_tokens=3500)
        
        # Extract the key sections from the response
        concept_analysis = extract_section(response, "concept_analysis")
        visualization_approach = extract_section(response, "visualization_approach")
        key_visual_elements = extract_section(response, "key_visual_elements")
        
        return {
            "concept_analysis": concept_analysis,
            "visualization_approach": visualization_approach,
            "key_visual_elements": key_visual_elements,
            "full_response": response
        }
    
    def design_scene(self, math_topic, audience_level="high school", concept_analysis=None):
        """Generate an animation design for a given math topic"""
        formatted_prompt = DESIGN.format(
            topic=math_topic,
            audience_level=audience_level
        )
        
        # If we have a concept analysis, include it in the prompt
        if concept_analysis:
            formatted_prompt += f"\n\n<concept_analysis>\n{concept_analysis}\n</concept_analysis>"
        
        response = self._send_prompt(formatted_prompt, max_tokens=3500)
        
        # Extract the animation design section
        animation_design = extract_section(response, "animation_design")
        self_evaluation = extract_section(response, "self_evaluation")
        
        return {
            "animation_design": animation_design,
            "self_evaluation": self_evaluation,
            "full_response": response
        }
    
    def test_animation_design(self, math_topic, animation_design):
        """Test an animation design for potential issues"""
        formatted_prompt = ANIMATION_TESTING.format(
            topic=math_topic,
            animation_design=animation_design
        )
        
        response = self._send_prompt(formatted_prompt, max_tokens=3000)
        
        # Extract the key sections
        novice_viewer = extract_section(response, "novice_viewer")
        expert_viewer = extract_section(response, "expert_viewer")
        cognitive_load = extract_section(response, "cognitive_load_analysis")
        improvements = extract_section(response, "design_improvements")
        
        return {
            "novice_viewer": novice_viewer,
            "expert_viewer": expert_viewer,
            "cognitive_load": cognitive_load,
            "improvements": improvements,
            "full_response": response
        }
    
    def generate_code(self, design):
        """Generate Manim code based on the design"""
        formatted_prompt = CODE_GENERATION.format(design_scene=design)
        response = self._send_prompt(formatted_prompt, max_tokens=5000)
        
        # Extract only the code portion, removing any self-evaluation or other content
        clean_code = extract_code_only(response)
        self_evaluation = extract_section(response, "code_self_evaluation")
        
        return {
            "code": clean_code,
            "self_evaluation": self_evaluation,
            "full_response": response
        }
    
    def process_feedback(self, math_topic, original_code, user_feedback, feedback_tags=None):
        """Process user feedback and improve the animation"""
        if feedback_tags is None:
            feedback_tags = ""
            
        formatted_prompt = FEEDBACK_INTEGRATION.format(
            topic=math_topic,
            original_code=original_code,
            user_feedback=user_feedback,
            feedback_tags=feedback_tags
        )
        
        response = self._send_prompt(formatted_prompt, max_tokens=4000)
        
        # Extract the key sections
        feedback_analysis = extract_section(response, "feedback_analysis")
        improvements = extract_section(response, "proposed_improvements")
        improved_code = extract_code_only(response)
        improvement_summary = extract_section(response, "improvement_summary")
        
        return {
            "feedback_analysis": feedback_analysis,
            "proposed_improvements": improvements,
            "improved_code": improved_code,
            "improvement_summary": improvement_summary,
            "full_response": response
        }
    
    def complete_workflow(self, math_topic, audience_level="high school", user_feedback=None):
        """Run the complete animation generation workflow"""
        # Step 1: Analyze the concept
        concept_results = self.analyze_concept(math_topic, audience_level)
        
        # Step 2: Design the animation
        design_results = self.design_scene(
            math_topic, 
            audience_level, 
            concept_results["concept_analysis"]
        )
        
        # Step 3: Test the animation design
        test_results = self.test_animation_design(
            math_topic,
            design_results["animation_design"]
        )
        
        # Step 4: Generate code based on design and test feedback
        enhanced_design = design_results["animation_design"] + "\n\n" + test_results["improvements"]
        code_results = self.generate_code(enhanced_design)
        
        # Step 5: If we have user feedback, process it
        if user_feedback:
            feedback_results = self.process_feedback(
                math_topic,
                code_results["code"],
                user_feedback
            )
            final_code = feedback_results["improved_code"]
            summary = feedback_results["improvement_summary"]
        else:
            final_code = code_results["code"]
            summary = "Initial animation generated without user feedback."
        
        return {
            "concept_analysis": concept_results,
            "animation_design": design_results,
            "design_testing": test_results,
            "code_generation": code_results,
            "final_code": final_code,
            "summary": summary
        }