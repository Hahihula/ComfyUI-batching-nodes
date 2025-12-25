# ComfyUI Batching Nodes - Examples & Tutorials

This document provides detailed examples and tutorials for using the ComfyUI Batching Nodes.

## Table of Contents

- [Prompt Batching Examples](#prompt-batching-examples)
- [Image Batching Examples](#image-batching-examples)
- [Combined Batching Examples](#combined-batching-examples)
- [Advanced Techniques](#advanced-techniques)

## Prompt Batching Examples

### Example 1: Generate Character Variations

**Goal:** Create 4 different character portraits

**Workflow:**

1. Add **Batch Text** node
2. Enter prompts:

```
a warrior in plate armor, fantasy art, detailed
a mage with staff, mystical aura, fantasy art, detailed
a rogue in leather armor, fantasy art, detailed
a cleric with holy symbol, fantasy art, detailed
```

3. Connect to CLIP Text Encode → Checkpoint → KSampler → VAE Decode → Save Image
4. Queue once → Get 4 images automatically!

**Tip:** Use consistent formatting across prompts for style consistency.

---

### Example 2: Test Different Art Styles

**Goal:** See the same subject in different artistic styles

**Workflow:**

1. Add **Batch Text** node with delimiter `,`
2. Enter prompts:

```
oil painting style, portrait of a cat, classical art
watercolor style, portrait of a cat, soft colors
digital art style, portrait of a cat, vibrant
pencil sketch style, portrait of a cat, detailed lines
```

3. Connect to your standard workflow
4. Use same seed for all to compare styles fairly

**Result:** 4 images of the same subject in different styles

---

### Example 3: Product Description Variations

**Goal:** Generate product images with different descriptions

**Workflow:**

1. Add **Batch Text** node
2. Enter prompts:

```
professional product photography, studio lighting, white background
product in natural environment, outdoor setting
lifestyle product shot, in use, realistic
product detail close-up, macro photography
```

3. Process through your workflow

---

## Image Batching Examples

### Example 4: Upscale Entire Photo Collection

**Goal:** Upscale 50 vacation photos at once

**Workflow:**

1. Add **Batch Images** node
2. Set `folder_path`: `/path/to/vacation_photos`
3. Set `image_extensions`: `jpg,jpeg`
4. Set `sort_by`: `name`
5. Set `max_images`: `0` (all images)
6. Connect: Batch Images → VAE Encode → Upscale Model → VAE Decode → Save Image
7. Queue once → All 50 photos processed!

**Time saved:** Instead of 50 manual loads, just one click!

---

### Example 5: Apply Face Restoration to Generated Images

**Goal:** Fix faces in a batch of AI-generated images

**Workflow:**

1. Place generated images in folder: `/input/faces_to_fix`
2. Add **Batch Images** node
3. Set `folder_path`: `/input/faces_to_fix`
4. Connect: Batch Images → Face Restore Node → Save Image
5. All faces fixed automatically

---

### Example 6: Convert Image Format in Batch

**Goal:** Convert 100 WebP images to PNG

**Workflow:**

1. Add **Batch Images** node
2. Set `folder_path`: `/input/webp_images`
3. Set `image_extensions`: `webp`
4. Connect: Batch Images → Save Image (with PNG format)
5. All converted in one go!

---

### Example 7: Process Only Recent Photos

**Goal:** Process photos from last week only

**Workflow:**

1. Add **Batch Images** node
2. Set `folder_path`: `/input/all_photos`
3. Set `sort_by`: `modified`
4. Set `max_images`: `20` (or however many you expect)
5. Process newest first

---

## Combined Batching Examples

### Example 8: Style Transfer Matrix

**Goal:** Apply 3 different styles to 5 different images (15 total outputs)

**Workflow:**

1. Add **Batch Text** node with 3 style prompts:

```
in the style of Van Gogh, impressionist
in the style of Picasso, cubist
in the style of Monet, post-impressionist
```

2. Add **Batch Images** node pointing to folder with 5 images

3. Connect both to your style transfer workflow

4. Result: 3 styles × 5 images = 15 unique combinations!

**Matrix visualization:**

```
              Image1   Image2   Image3   Image4   Image5
Van Gogh        ✓        ✓        ✓        ✓        ✓
Picasso         ✓        ✓        ✓        ✓        ✓
Monet           ✓        ✓        ✓        ✓        ✓
```

---

### Example 9: A/B Testing Prompts on Same Images

**Goal:** Test which prompt works better on your test images

**Workflow:**

1. **Batch Text** with 2 prompt variations:

```
high quality, detailed, professional photography
ultra realistic, 8k, photorealistic, award winning
```

2. **Batch Images** with 10 test images

3. Connect both to KSampler with **SAME SEED**

4. Result: 20 images (2 prompts × 10 images) to compare

---

### Example 10: Product Mockup Generator

**Goal:** Place product in different environments

**Workflow:**

1. **Batch Images**: Product photos from different angles (3 images)
2. **Batch Text**: Different environment descriptions (4 prompts)

```
in modern kitchen, bright lighting
in cozy living room, warm atmosphere
in professional office, clean design
in outdoor garden, natural light
```

3. Connect both to ControlNet workflow
4. Result: 12 product mockups (3 angles × 4 environments)

---

## Advanced Techniques

### Technique 1: Resume Interrupted Batches

If your batch processing was interrupted:

**Workflow:**

1. Check how many images were already processed
2. Use `start_index` to skip processed images
3. Continue from where you left off

**Example:**

```
First run: max_images: 50, start_index: 0   → Process images 0-49
Interrupted at image 30!
Resume run: max_images: 0, start_index: 30  → Process images 30-end
```

---

### Technique 2: Process in Chunks for Memory Management

For very large batches:

**Workflow:**

1. First chunk: `start_index: 0, max_images: 100`
2. Second chunk: `start_index: 100, max_images: 100`
3. Third chunk: `start_index: 200, max_images: 100`
4. Continue until done

---

### Technique 3: Organized File Naming

Use the filenames output for smart saving:

**Workflow:**

1. **Batch Images** → outputs both `images` and `filenames`
2. Use a String manipulation node to modify filename
3. Pass modified filename to Save Image node
4. Result: Organized output with meaningful names

---

### Technique 4: Conditional Processing

Process only certain images based on properties:

**Pseudo-workflow:**

1. Load images with Batch Images
2. Use image dimensions checker (custom node)
3. Filter to only portrait orientation
4. Process filtered batch

---

### Technique 5: Delimiter Tricks

**Comma-separated for CSV-like input:**

```
Delimiter: ","
Input: "cat, sitting, indoors, cute, cat, playing, outdoors, energetic"
Result: 4 prompts (assuming word pairs)
```

**Multi-line for complex prompts:**

```
Delimiter: "\n\n"  (double newline)
Input: "A detailed description
that spans multiple lines
for one prompt.

A second detailed description
also spanning lines
for the second prompt."
Result: 2 prompts
```

---

## Tips for Best Results

### For Prompt Batching:

- Keep prompts similar in structure for consistency
- Use the same seed to isolate prompt variations
- Test with 3-5 prompts first before large batches
- Include quality tokens in all prompts if needed

### For Image Batching:

- Name files with leading zeros for proper sorting (001, 002, etc.)
- Test with `max_images: 5` first to verify workflow
- Use absolute paths for `folder_path`
- Check console for loading confirmation messages

### For Combined Batching:

- Understand multiplication: N prompts × M images = N×M outputs
- Start small (2×2 = 4) to test before large matrices
- Monitor memory usage
- Use consistent seeds for fair comparisons

---

## Common Workflows Summarized

| Goal                       | Nodes Used   | Key Settings                      |
| -------------------------- | ------------ | --------------------------------- |
| Multiple prompt variations | Batch Text   | Different prompts, same settings  |
| Upscale folder of images   | Batch Images | max_images: 0                     |
| Test styles on one subject | Batch Text   | Same subject, different styles    |
| Process recent photos      | Batch Images | sort_by: modified, max_images: N  |
| Style transfer matrix      | Both nodes   | Multiple styles × multiple images |
| Resume interrupted batch   | Batch Images | start_index: N                    |
| Convert image formats      | Batch Images | Load one format, save another     |
| Character sheet generation | Batch Text   | Different angles/views            |

---

## Getting Help

If you need help with any of these examples:

1. Check the console for error messages
2. Verify your node connections
3. Start with simple examples first
4. Open an issue on GitHub with your workflow JSON

Happy batching! 🚀
