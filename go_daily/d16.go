// YOUR NAME HERE
// DATE HERE

package main

import (
	"fmt"
	"net"
	"bufio"
)

func queryServer(query, service string, c chan string) {
    // use net.Dial to make a tcp connection to service
    // (or if your initials are "JC" you may be dialing moscow service instead)

    // check to be sure that the dialing connected properly
    // be sure that your call to net.Dial saves the error in a variable err
    if err != nil {
        fmt.Println("error: ", err)
    }

    // use fmt.Fprintf to send the query over the connection

    // create a new Reader using bufio.NewReader() for the connection

    // create an empty string variable
    resp := ""

    // use the reader to read a line
    line, err := reader.ReadString('\n')

    // loop until there are no more lines to read
    for (line != "") {
        resp += line
        line, err = reader.ReadString('\n')
    }

    // write the string resp to the channel
}

func main() {
    // first make a channel for strings

    // call queryServer in a goroutine once for each query

    // read from the channel twice, once to collect data from each goroutine
    // remember that the channel will block on the read until the channel is written to by one of the goroutines
    // save the responses as string variables resp1 and resp2

    // print out the resp1 and resp2
    fmt.Println("=================== RESPONSE 1 ===================\n")
    fmt.Println(resp1)
    fmt.Println("\n=================== RESPONSE 2 ===================\n")
    fmt.Println(resp2)
    fmt.Println("\n==================================================")

    // correct output will have the complete HTTP response from both requests
    // note that the ORDER might vary depending on which goroutine writes to the channel first
    /*
        =================== RESPONSE 1 ===================
        
        HTTP/1.1 200 OK
        Server: CherryPy/8.1.2
        Access-Control-Allow-Methods: GET, PUT, POST, DELETE, OPTIONS
        Access-Control-Allow-Origin: *
        Content-Length: 134
        Content-Type: text/html;charset=utf-8
        Date: Thu, 27 Apr 2017 19:43:18 GMT
        Access-Control-Allow-Credentials: true

        {"id": 32, "result": "success", "genres": "Drama|Sci-Fi", "img": "/vxiIABQhiFlfODwamoevrzXvowU.jpg", "title": "Twelve Monkeys (1995)"}
        
        =================== RESPONSE 2 ===================
        
        HTTP/1.1 200 OK
        Server: CherryPy/8.1.2
        Access-Control-Allow-Methods: GET, PUT, POST, DELETE, OPTIONS
        Access-Control-Allow-Origin: *
        Content-Length: 67
        Content-Type: text/html;charset=utf-8
        Date: Thu, 27 Apr 2017 19:43:18 GMT
        Access-Control-Allow-Credentials: true

        {"result": "success", "rating": 3.9450694904037062, "movie_id": 32}
        
        ==================================================
     */
}
