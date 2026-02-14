# Photo Classification Project Report

## Why I Took This Approach

The task requirements were:

-   Small dataset (30--35 photos)\
-   7 real-world classification tags\
-   Must run smoothly on a normal laptop\
-   No model training required\
-   Output should automatically sort photos into folders

Because of these constraints, the best solution is a **Hybrid AI +
Classical Computer Vision Pipeline**.

Instead of training a large deep learning classifier from scratch, we
combine:

-   Face detection\
-   Blur detection\
-   Smile detection\
-   Animal recognition\
-   Simple rule-based logic

This is the same type of lightweight pipeline used in many real-world
photo apps.

------------------------------------------------------------------------

## Why Not Use One Big Classification Model?

A single deep learning model works well for object categories such as:

-   Cat
-   Dog
-   Car

But our required tags are **semantic photo categories**, such as:

-   Eyes Closed
-   Blurry
-   Solo vs Group
-   No Humans
-   Smiling

Pretrained classifiers do not directly output these categories.
So the problem requires multiple detectors working together.

------------------------------------------------------------------------

## Models Used and Reason

### 1. MediaPipe Face Detection

**Used for:**

-   Solo portraits
-   Group photos
-   No-human photos

**Why chosen:**

-   Very fast
-   Runs efficiently on CPU
-   Accurate face counting

**Limitation:**

-   Misses faces if they are:
    -   Too small
    -   Side-view
    -   In dark lighting

So some images may not be classified correctly.

------------------------------------------------------------------------

### 2. OpenCV Blur Detection (Laplacian Variance)

**Used for:**

-   Blurry photos

**Why chosen:**

-   Very simple mathematical method
-   No AI model required
-   Works reliably for motion/out-of-focus blur

**Limitation:**

-   Cannot detect:
    -   Artistic blur
    -   Background blur (portrait mode)

------------------------------------------------------------------------

### 3. OpenCV Smile Haar Cascade

**Used for:**

-   Smiled photos

**Why chosen:**

-   Lightweight
-   No TensorFlow dependency
-   Runs fully offline

**Limitation:**

-   Less accurate than deep emotion models
-   Fails if:
    -   Smile is small
    -   Face angle is tilted

------------------------------------------------------------------------

### 4. MobileNetV2 (Animal Detection)

**Used for:**

-   Animals

**Why chosen:**

-   Pretrained on ImageNet
-   Small and efficient
-   Works without training

**Limitation:**

-   Sometimes misclassifies:
    -   Stuffed toys
    -   Unclear pets
    -   Partial animal bodies

------------------------------------------------------------------------

## Conclusion

This hybrid approach provides an efficient and practical solution:

-   Runs on CPU
-   Requires no training
-   Modular and easy to improve
-   Extensible to more powerful deep learning models for higher accuracy requirements
-   Matches real-world lightweight photo classification systems

Some photos remain unclassified due to detection confidence limits and
ambiguity, which is expected in rule-based pipelines.

------------------------------------------------------------------------
