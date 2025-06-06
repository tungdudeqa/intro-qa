# Test plan

A document containing details about all the testing-related activities, like how to test, who will test, test type to use, etc.

#### Creating a test plan

1. Analyze the product to understand the requirements and how it works
2. Design test strategy
    - scope what to test and what to pass
    - type of testing to be used
3. Define test objectives and the expected outcomes
4. Define test criteria
    - Suspension criteria: conditions that test should be halted to avoid wasting resources at a critical moment
    - Exit criteria: conditions to meet before moving to the next stage of SDLC
5. Resource planning such as human effort, hardware / software, infrastructure, etc.
6. Plan test environment
7. Test schedule and time estimation
8. Determine risks and mitigations that might happen during testing

#### Types of tests

1. White box testing
    - Test the internal of the software. Tester has access to the source code
2. Black box testing
    - Test the functionality of the software without knowledge of how it works internally
3. Gray box testing
    - Tester has some knowledge about the internal structure
4. Unit tests
    - Test individual functions / methods of components, classes, or modules in the software
5. Integration tests
    - Test that each modules or services work well together
6. System tests
    - Test the complete system
7. End-to-end tests
    - Test the whole user flow of an action
8. Acceptance testing
    - Test that the system meets the acceptance criteria to enable the customer to accept the system
9. Performance testing
    - Test the performance of the system under a particular amount of workload. Can measure reliability, speed, scalability, responsiveness, etc.
10. Smoke testing
    - Test basic and critical functionalities of a software to make sure that it is stable enough for further testing. If smoke testing fails, further tests will be suspended
11. Regression testing
    - Test that new features does not break the existing features.
12. Compatibility testing
    - Test that the software is compatible with different environments sucha as browsers
13. A/B Testing
    - Test two variants of the same content to compare which is better
14. API Testing
    - Test the functionality of API

# CI/CD Pipeline
Code change -> Trigger build -> Tests -> Move to staging -> Deploy to production if good enough -> Operate -> Monitor -> Repeat