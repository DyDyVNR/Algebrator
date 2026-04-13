# Project Draft 1: Stand Up Meeting

Stand up meetings are one of the fundamental parts of agile development, and it’s often the most misunderstood. Let’s be real: stand-ups by themselves don’t make your team agile. They aren’t about inflating egos or justifying job descriptions. They aren’t a time to plan; Sprint planning is for planning. They also aren’t the only time to mention blockers. If you’re stuck, ask for help! Want to learn more, then read the article: [What is a stand up meeting & tips to run one](https://www.atlassian.com/agile/scrum/standups)

In this project draft, you will be answering a variation of the three questions normally asked during an agile Stand Up Meeting as part of the SDLC process. Simply remove the text that says *YOUR ANSWER HERE* and answer the questions below.

## Question 1: What have I worked on since the start of the project?

I have worked on creating the base structures and several classes in different py files. I first started working on matrix.py to have an idea of how I was going to decide my matrix structure. As I was working on Matrix class, I started to notice I needed more classes like exceptions to raise some customized errors and helper class to handle other functions such as prompting the user inputs and calling sepcific operations to use. Throughout this process, I've been implementing fundamental operations such as matrix addition, subtraction, multiplication, transpose, and inverse. I've also focused on error handling to ensure the program can manage invalid inputs appropriately. Additionally, I've been testing these implementations boht manually and with unit testing with various matrix dimensions to verify correctness and identify edge cases like dimensional errors. 

## Question 2: What am I working on between now and the next draft check-in?

Between now and the next draft check-in, I will be working on:
* completing row-reduce-echelon method in matrix.py along with its unit testing.
* completing the rest of operation methods in helper.py file. 
* polishing my user prompts such that each invalid input is handled appropriately.

## Question 3: What issues are blocking me?

So far there has been no big issues that are blocking me. The only issue I have been having is the decision making. For example, I was debating whether I should use recursion or iteration for some of the matrix methods. Recursion can be easier to implement but consumes significant memory espcially if we operate on a 9x9 matrix or larger, but due to the time constraint I'm having right now, perhaps I considered it as well. Therefore, the actual issue I have is lack of time. 
