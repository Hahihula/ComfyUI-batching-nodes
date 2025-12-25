"""
ComfyUI Custom Node: Prompt Loop
This node splits input text by a delimiter and processes each line through the workflow
"""

class PromptLoopNode:
    """
    A node that takes a multi-line string, splits it by delimiter,
    and outputs each line sequentially for batch processing
    """
    
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {
                    "multiline": True,
                    "default": "prompt 1\nprompt 2\nprompt 3"
                }),
                "delimiter": ("STRING", {
                    "multiline": False,
                    "default": "\n"
                }),
                "skip_empty": ("BOOLEAN", {
                    "default": True
                }),
            }
        }
    
    RETURN_TYPES = ("STRING", "INT",)
    RETURN_NAMES = ("prompts_list", "count",)
    OUTPUT_NODE = False
    OUTPUT_IS_LIST = (True, False,)
    
    FUNCTION = "split_prompts"
    CATEGORY = "text"
    
    def split_prompts(self, text, delimiter="\n", skip_empty=True):
        """
        Split the input text by delimiter and return as list
        
        Args:
            text: Input string to split
            delimiter: Character(s) to split by (default: newline)
            skip_empty: Whether to skip empty lines (default: True)
        
        Returns:
            tuple: (list of prompts, count of prompts)
        """
        # Split text by delimiter
        prompts = text.split(delimiter)
        
        # Optionally remove empty strings
        if skip_empty:
            prompts = [p.strip() for p in prompts if p.strip()]
        else:
            prompts = [p.strip() for p in prompts]
        
        count = len(prompts)
        
        return (prompts, count)


class PromptFromListNode:
    """
    A node that extracts a single prompt from a list by index
    Useful for processing one prompt at a time in a loop
    """
    
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "prompts_list": ("STRING", {"forceInput": True}),
                "index": ("INT", {
                    "default": 0,
                    "min": 0,
                    "max": 10000
                }),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    OUTPUT_NODE = False
    INPUT_IS_LIST = True
    
    FUNCTION = "get_prompt"
    CATEGORY = "text"
    
    def get_prompt(self, prompts_list, index):
        """
        Get a specific prompt from the list by index
        
        Args:
            prompts_list: List of prompts
            index: Index to retrieve (0-based)
        
        Returns:
            Single prompt string
        """
        # Handle the input format
        if isinstance(index, list):
            index = index[0]
        
        if isinstance(prompts_list, list) and len(prompts_list) > 0:
            # Make sure index is within bounds
            actual_index = index % len(prompts_list)
            return (prompts_list[actual_index],)
        
        return ("",)


# Node registration
NODE_CLASS_MAPPINGS = {
    "PromptLoopNode": PromptLoopNode,
    "PromptFromListNode": PromptFromListNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PromptLoopNode": "Batch Text (Prompt Loop)",
    "PromptFromListNode": "Get Prompt From Batch",
}

WEB_DIRECTORY = "./web"

# Debug output to confirm loading
print("\n" + "="*50)
print("Prompt Loop Node - Loading...")
print(f"Registered nodes: {list(NODE_CLASS_MAPPINGS.keys())}")
print("="*50 + "\n")