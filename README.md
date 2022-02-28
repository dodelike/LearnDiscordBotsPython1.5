# LearnDiscordBotsPython1.5
This script is for teaching the basics of using the "random" library. The script will be a simple coin flipping program, requiring user input. This is a .5 due to not yet working with a Discord Bot. The next installment will iterate the discord library to complete the same program, running on your Discord Server.

## What We Accomplish
### Random Generation
```import random```</br></br>
This is used to import the random library, which is built into Python. On the other end, like in LDBP1, we imported discord. We needed to install the Discord library via command line as this is not built into Python. Python has many other built in libraries we should be using in the future that do not require manual installing.</br>
### User Input
The ```input``` function is used to ask for user input. In this program, the console asks "Heads or Tails?" and awaits user input. You should also notice we added ```.lowercase()``` at the end of the input string in order to convert any text input from the use as lowercase to match what we declared in the earlier variable. Without this, a user entering Tails or HEAdS would not explicitly match what we declared in ```coin``` and thus always declare the user a loser.
