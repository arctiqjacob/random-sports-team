package main

import "fmt"

type Team struct {
	name string
	year int
	arena string 
}

func main() {	
	teamA := Team{"Toronto Maple Leafs", 1917, "Scotiabank Arena"}
	teamB := Team{"Toronto Raptors", 1995, "Scotiabank Arena"}
	teamC := Team{"Toronto FC", 2005, "BMO Field"}
	teamD := Team{"Toronto Blue Jays", 1977, "Rogers Centre"}
	teamE := Team{"Toronto Argonauts", 1873, "BMO Field"}
	teamF := Team{"Toronto Rock", 1999, "Scotiabank Arena"}
	
	teams := [6]Team{teamA, teamB, teamC, teamD, teamE, teamF}
	fmt.Println(teams)
}
