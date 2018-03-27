# Boobook
Boobook SCADA written in [Python][]/[Kivy][] for the graphical development
part, and [C][], [Guile][] or [Rust][] for the server part. The last one
is not decided on yet.

[Python]: https://www.python.org
[Kivy]: https://kivy.org
[C]: https://www.gnu.org/software/libc/
[Guile]: https://www.gnu.org/software/guile/
[Rust]: https://www.rust-lang.org/

# Background
My name is Michael Isberg and I work as a senior [SCADA][] system engineer.
I have been programming [PLC][]'s of many different brands and integrating
in different SCADA systems for twelve years now.
My main interest is GNU/Linux and with it I spend much of my spare time.

The automation business is totally Microsoft Windows dominated, at least
with regard to development tools for PLC's and SCADA systems. These are
oftentimes expensive and not so rarely buggy. With this in mind, and with
the knowledge that free software and the community around it is much more
fun, I have had a dream of writing a completely free SCADA system,
preferably with the help of others.

I have had this dream for many years now and it will probably be a dream
for many more years, if not until the end of my lifetime.
But the journey is half the fun and it also being a dream makes it a 
whole more fun.

The name Boobook is Latin for a species owls living in Australia. I was
thinking of using the name Bombus, Latin for bumblebee, since I think
it's a beautiful and interesting animal. But since that domain name was
taken, I chose a similar name, and Boobook it was.

[SCADA]: https://en.wikipedia.org/wiki/SCADA
[PLC]: https://en.wikipedia.org/wiki/Programmable_logic_controller

# Introduction
SCADA stands for Supervisory Control And Data Acquisition. It's a type of
software used for acquiring data from mainly PLC's (Programmable Logic 
Controller) through supported communication protocols. But every device
that supports the same communication protocol as the SCADA system can
be used. If there's no native support for a communication protocol in the
SCADA system oftentimes this is solvable with the use of a third party
software called [OPC][]. This acts as a server communicating with many
different types of PLC's, depending on it's supported protocols, and
exposes a single interface to the SCADA system. I'm not sure if there's
an available GNU/Linux OPC server out there. I think that one problem
with this solution could be that the communications protocols for the
different brands of PLC's a proprietary.
This can be solved by the fact that every serious PLC brand out there
supports the [Modbus][] communication protocol which has become a
_de facto_ standard.

[OPC]: https://en.wikipedia.org/wiki/Open_Platform_Communications
[Modbus]: https://en.wikipedia.org/wiki/Modbus

# Setup
I was thinking of dividing this software into three parts:
1. The graphical development environment (**GDE**) system written in
Python/Kivy for easiness. The name of this is my idea and nothing
which is used officially. Every SCADA system uses their own setup and
naming.
2. The servers, I/O, alarm, trend and maybe report, written in C, Guile
or Rust depending on a couple of different things which are not all yet
clear at this moment.
3. The client will also be written in Python/Kivy.

## The GDE
The GDE will at first only consist of two parts, the tree view at the
left for showing graphical pages, graphical objects, compound graphical
objects and server.
I was also thinking of saving the pages as .svg files although I don't
know if there's also a possibility to also save the events of the graphical
objects in the same file.

## The servers
The servers will all be implemented in the same piece of software with the
possibility to turn them on/off according to the usage. Values read from
devices are stored in what is called tags in the servers. And so there can
be I/O tags, alarm tags, trend tags and so on. But I was thinking of having
just on tag for all these and creating alarms and trends depending on which
fields in the tag list are filled in.
At first I would like to implement these features:
* Redundancy with the possibility for clients to switch server depending on
which one is alive.
* Synchronization between servers as they come online again.
* Internal load balancing for dividing the PLC's on different threads
depending on their latency.

## The client
Clients will display the information implemented in the GDE and update the
view depending on the status of tags they read from the I/O servers.
I'm hoping that the clients can be runnable in a smart phone.

# Contribution
If you have any ideas or feel that you want to help me out please feel free
to contact me at michael DOT isberg AT posteo DOT de.

# Other
This a living document and will be updated as new ideas come to mind or I
change my mind about if and how to implement a feature.