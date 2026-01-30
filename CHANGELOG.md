# Changelog

## 2026

- I'm rewriting the first few lessons so that they are self-contained. Originally they relied more on self learning, but we have observed an increasing student preference towards directed material.
  - In L3, I equalized the explanation of the RR planar robot with the later lessons. 
  - In L3, I added a section about FKM based on a DH table. 
- I am adding exercises and solutions to those exercises for each lesson. More examples will be added when needed.

## 2025

- I'm removing `spatialmath` from the tutorials and moving any old content to `legacy/spatialmath`. The original intention when adding this library was to facilitate more complex content in later parts of the module. With variable levels of programming knowledge in the standard cohort this is not possible, and the following issues were observed:
   - `spatialmath` not being available as binary package in many distributions, causing students to have to compile the `wheel` even when using `pip`. 
        - In Windows enviroments, for example, this means having a working VS Compiler installation which is not default and is beyond the scope of this module. 
        - In any distribution, this could take several minutes and even fail depending on student's enviroments.
   - Students tend to default to memorising the library functions instead of understanding the underlying mechanism, irrespective of how trivial the operations are. It is more pedagogical to rely on the matricial operations that they are expected to learn and reinforce that knowledge.

- Remove all mentions of `import` in sample code, and keep them to explicit and isolated import cells. Despite the clear indication in the text that the `import` statement was merely illustrative, novice readers often default to copying and pasting chunks of example code causing extraneous `import` statements that result in unprofessional code that, beyond aesthetics, can cause all sorts of issues.
