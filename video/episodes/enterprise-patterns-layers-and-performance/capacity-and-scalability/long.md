---
format: long
lesson: enterprise-patterns-layers-and-performance/capacity-and-scalability
title: Swordfish and Camel: capacity isn't scalability
thumb: More capacity, less scale
---

@chapter The loose word
@title text="Capacity and Scalability" sub="Patterns of Enterprise Application Architecture, Introduction" art=thumb
Of all the performance words people use loosely, Martin Fowler says scalability is the worst. So he pins it down, alongside two words it gets confused with: efficiency and capacity.

@quote text="Scalability is a measure of how adding resources (usually hardware) affects performance." cite="Fowler, Patterns of Enterprise Application Architecture, Introduction"
Here's his definition. Scalability is a measure of how adding resources, usually hardware, affects performance.

@chapter Three terms
@math heading="Efficiency = performance ÷ resources" items="30 tps ÷ 2 CPUs = 15 a CPU@thirty transactions;;40 tps ÷ 4 CPUs = 10 a CPU@forty on four"
Efficiency is performance divided by resources. Thirty transactions a second on two CPUs is fifteen a CPU. Forty on four identical CPUs is ten a CPU. So the first is more efficient, even though forty is the higher throughput.

@art capacity-ceiling
Capacity is the maximum effective throughput or load. That might be an absolute maximum, or the point where performance drops below what's acceptable.

@art scale-up
And scalability is what more hardware adds. A scalable system gives a commensurate gain, like twice the throughput for twice the servers. Scaling up, or vertical scalability, means adding power to one server, such as more memory.

@art scale-out
Scaling out, or horizontal scalability, means adding servers.

@chapter Swordfish and Camel
@math heading="One server" items="Swordfish: 20 tps@Swordfish handles;;Camel: 40 tps@Camel forty"
Now Fowler's illustration. Two systems run on one server. Swordfish handles twenty transactions a second, Camel forty. Which performs better, and which scales better? He says the second can't be answered from these figures, and the first only partly. Camel is more efficient on one server.

@math heading="Add servers" items="2 servers: Swordfish 35, Camel 50@Add a server;;gain: Swordfish +15, Camel +10 a server@Swordfish gains"
Add a server, and Swordfish handles thirty five, Camel fifty. Keep adding, and Swordfish gains fifteen a server, Camel only ten. These are the book's figures, posed as a supposition to make the point.

@math heading="Where they meet" items="Swordfish: 20 + 15 × 4 = 80@twenty plus;;Camel: 40 + 10 × 4 = 80@forty plus;;5 servers: both 80@five servers"
Project them out. At five servers, Swordfish is twenty plus fifteen times four, which is eighty. Camel is forty plus ten times four, also eighty. They meet at five servers. Swordfish has the better horizontal scalability, though Camel is more efficient below five.

@art two-lines-cross
So the system with more capacity on one server isn't the one that scales better. Capacity says what one configuration does. Scalability says what the next servers add.

@chapter Counting servers
@code block=1 lines=1-13 label=Java focus="3-5@guard|6-7@one server|8-11@add a server"
The lesson turns this into a count. Start with one server at its measured throughput, then add a server and its gain until you reach the target. The guard is there because a system that gains nothing from another server would keep the loop running for ever.

@math heading="Servers needed" items="target 40: Swordfish 3, Camel 1@forty a second;;target 120: Swordfish 8, Camel 9@a hundred and twenty;;at 10 servers: Swordfish 155, Camel 130@at ten servers"
At forty a second, Camel needs one server, Swordfish three. At a hundred and twenty, Swordfish needs eight and Camel nine, so the order has turned round. And at ten servers, Swordfish handles a hundred and fifty five to Camel's hundred and thirty.

@chapter Build for scale
@art hardware-vs-effort
Fowler's conclusion is practical. It often makes sense to build for hardware scalability, rather than for capacity or even efficiency. Designers do complicated things to squeeze one platform when more hardware would be cheaper.

@words text="Hardware < programmers" sub="if the system can use it"
Hardware often costs less than the programmers it would take to do without it, as long as the system can use it. He admits he grumbles too, whenever he has to upgrade his laptop for the latest version of Word.

@chapter Where people slip
@list heading="Common slips" items="More capacity means it scales better@The first|Efficiency is throughput@The second|A projection is a measurement@And the third"
The first slip is thinking the system with more capacity scales better. The second is taking efficiency for throughput. And the third is reading a projection as a measurement.

@art scale-flat
The lab, like the book, carries each system on at the gain between two measurements. That's an assumption. Real systems can gain less with each server as they share a database or a network, and the crossover can move or vanish. The next measurement tells you whether the line holds.

@chapter Try it
@words text="Heron: 30 tps on 1, 54 on 3" sub="Stork: 45 tps on 1, 57 on 3"
Your turn. Heron does thirty a second on one server and fifty four on three. Stork does forty five on one and fifty seven on three. Find each one's gain a server, where heron first matches or passes stork, the servers each needs for sixty, and each one's throughput at six servers.

@end text="Project two systems yourself"
You can enter measurements and watch the lines cross, on Learn. That's learn dot get er done dot I O.
