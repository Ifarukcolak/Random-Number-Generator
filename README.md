# Random-Number-Generator
Generate Random Numbers Using LCG Method

## What is the random number generator ? 
A random number generator (RNG) is a mathematical construct, either computational or as a hardware device, that is designed to generate a random set of numbers that should not display any distinguishable patterns in their appearance or generation, hence the word random. (https://www.techopedia.com/definition/9091/random-number-generator-rng)

## Which features make random number generator that has good qualities ? 
  * High **periodicity**
  * High **independence**
  * High **uniformity**
  
## Hull-Dobell Theorem
Hull - Dobell Theorem is used make LCG Generator that has full period .

LCG has full period iff ,
  * The highest common multiple of m and c is 1.
  * If m is a multiple of a prime number p then a-1 must also be a multiple of p.
  * Whenever m is a multiple of 4, a-1 must be a multiple of 4.
  
  



Thanks to  Damien Jade Duff for the Discrete Event Simulation Lesson (http://djduff.net/).
