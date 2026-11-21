---
format: long
lesson: enterprise-patterns-distribution/plugin-and-service-stub
title: Plugin and Service Stub: test without the slow service
thumb: Choose the implementation once
---

@chapter The problem
@title text="Plugin and Service Stub" sub="Patterns of Enterprise Application Architecture, Chapter 18" art=thumb
Your signup checks a postcode with a remote post office service. Now your tests need the network. Two small patterns fix that, and each needs the other.

@quote text="Use Service Stub whenever you find that dependence on a particular service is hindering your development and testing." cite="David Rice, in Fowler, Patterns of Enterprise Application Architecture, Chapter 18, Service Stub"
Here's David Rice's rule. Use Service Stub whenever you find that dependence on a particular service is hindering your development and testing.

@chapter Plugin
@art factory-mess
Plugin, by Rice and Matt Foemmel, starts from Separated Interface. Code in several environments needs a different implementation in each. The usual answer is a factory with a conditional on the environment. Once there are a few such factories, you have a mess. A new configuration means editing several, rebuilding, and redeploying.

@art one-config-point
So a Plugin states its linking instructions at one external point, like a text file mapping each interface to an implementation, and links them at run time. It works best with reflection, so the factory needn't depend on the implementations at compile time. Without reflection, one central point is still worth having.

@chapter Service Stub
@art slow-service
Service Stub starts from the services you lean on and don't control, like credit scoring or pricing engines. Being remote, they can be slow and unreliable. Developers wait, or hack around them. Worse, tests can't run, which Rice says breaks the development process.

@art gateway-interface
The steps are the two earlier patterns. Reach the service through a Gateway, and make the Gateway a Separated Interface. One implementation calls the real service. Another is the stub, running locally, fast, in memory. And load the right one with a Plugin.

@words text="As simple as possible" sub="a complicated stub defeats the point"
Keep the stub as simple as possible, a few lines. A complicated stub defeats the point. Rice notes that many Extreme Programming practitioners call this a Mock Object. He kept Service Stub because the name is older.

@chapter The code
@code block=1 lines=1-20 label=Java focus="2-4@the Separated Interface|5-9@the stub|12-20@the plugin"
Here are all three parts. First, the Separated Interface: is this postcode deliverable? Then the stub, which says yes to every postcode except those beginning Z Z, so a test can ask for either answer. Then the plugin, one switch on the environment, read once at startup.

@words text="Solves the scattering, not the rebuild"
It's the one place that knows both implementations. But a new environment, say a staging setup that uses the stub, is still a change to this code. A configuration file read at startup, or reflection, would remove that.

@chapter Count the reach
@art ripple-direct
The lab walks dependencies backwards. With the real service, the signup calls the post office, which uses the network library, and the test calls the signup. Change the network, and it reaches one class directly, and three in all: the post office, the signup, and its test.

@math heading="plugin-and-stub: change network" items="direct: postofficecheck = 1@one directly;;reached: main, postofficecheck = 2@two in all"
Now wire it from the edge. The signup depends on the interface. The real check and the stub implement it. And main, the startup code that calls the plugin, depends on the real check. Change the network, and it reaches one directly and two in all. Neither the signup nor its test is reached.

@art ripple-edge
That depends on who calls the switch. If the signup called the plugin itself, it would depend on the plugin, which names the real check. Then a change to the network reaches four. So read the configuration at the edge, not inside the code that uses the interface.

@chapter Where people slip
@list heading="Common slips" items="A stub tests the service@The first|A plugin needs a framework@The second|Make the stub faithful@And the third"
The first slip is thinking a stub tests the service. It tests the code that uses it. The second is thinking a plugin needs a framework. It needs one place that chooses. And the third is making the stub faithful to the service. Then it's another thing to test and keep in step.

@chapter Try it
@words text="invoice → ratesfeed → http" sub="then: an interface, a stub, main wiring httprates"
Your turn. An invoice priced from an exchange rate feed, which uses http, and a test of the invoice. Change http. What does it reach? Then redesign it with an interface, a real implementation, a stub, and main wiring it up. Write the records, and say whether the test still needs the network.

@end text="Trace the dependency yourself"
You can paste dependency records into the lab and see what a change reaches, on Learn. That's learn dot get er done dot I O.
