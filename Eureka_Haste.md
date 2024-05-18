# Haste

Author: Anna Molkot@Leviathan<br>
Last Updated: 6 April 2024

Questions or suggestions?<br>
Contact me here: [THL/#eureka-general-chat](https://discord.com/channels/578708223092326430/816800750147207199)


## Description

Haste is a bonus found on certain pieces of gear orignating from Eureka.  Each piece of Eureka haste gear provides a "Haste +3" bonus, each point _directly_ reducing GCD and other cast and recast times by about 1%, each piece therefore reducing times by about 3%. It affects neither Skill Speed nor Spell Speed.
For those considering whether or not to use haste gear: consider reading [this guide](https://github.com/EurekaEnjoyer/Eureka_Guides/blob/main/Eureka_Gearing.md) and using the formula below before making a decision.
## Calculating GCDs

Exact calculation of GCDs with haste gear is simple.  In order to calculate this reduction, we will need to use a slightly edited version of the [Weaponskill and Spell Cast and Global Cooldown Reduction formula](https://www.akhmorning.com/allagan-studies/stats/speed/#formulae)
provided by Allagan Studies.  
Accounting for haste and plugging in specific level-70 modifiers gives us

$$\LARGE T\left(T_0, n, s\right) = \frac{1}{100} \left \lfloor \frac{T_0 \left(100 - N\right) \left(100 - B\right) \left(1000 - \left \lfloor  \frac{130}{900} \left (  S - 364 \right ) \right \rfloor \right)}{1000000} \right\rfloor$$ 

where <br>

$\large T = t\left(t_0, n, s\right)$ 		is the reduced action (re)cast time, in seconds;<br>
$\large T_{0}$            	            is the action (re)cast time in seconds, absent any speed or haste gear (for example, 2.5s for GCD);<br>
$\large N$ 						                  is the number of points of haste;<br>
$\large S \geq 364$ 						        is the skill/spell speed substat amount; and <br>
$\large \left \lfloor A \right \rfloor$ is the [floor function](https://mathworld.wolfram.com/FloorFunction.html) applied onto $A$.

### Example:

Suppose I have 3 points of haste and a skill speed of 603, and I wish to determine my current GCD.  We use the above formula and the information given to solve below:<br>

$\text{GCD} = T\left(2.5 \text{ s}, 3, 603\right) = 2.34 \text{ s}$
