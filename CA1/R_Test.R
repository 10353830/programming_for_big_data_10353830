print ('Hello World')

x  = 42
y<- x + 1
2^3
5/2
is.numeric('hi')
as.numeric('4')

#In Class Example – transform from Celsius To Fahrenheit
#celciusInput <- readline("please enter a Celcius value:")

toFahr = function(celciusInput){
  celciusNumeric <- as.numeric(celciusInput)
  fahrResults <- ((9/5)*celciusNumeric)+32
  fahrString <- sprintf("%.2f", fahrResults)
  message <- paste("the result is", fahrString, sep=" ")
  print(message)
}

toFahr(0)

x -42
if (x==42){
  print('x is 42')
 } else {
    print('x is not 42')
 }

myvector = c(1,2,3)
myvector = 4:6

for (count in c(1,2,3)){
  print (count)
}

#| When you are at the R prompt (>):
 # | -- Typing skip() allows you to skip the current
#| question.
#| -- Typing play() lets you experiment with R on your
#| own; swirl will ignore what you do...
#| -- UNTIL you type nxt() which will regain swirl's
#| attention.
#| -- Typing bye() causes swirl to exit. Your progress
#| will be saved.
#| -- Typing main() returns you to swirl's main menu.
#| -- Typing info() displays these options again.

#| Let's get started!
