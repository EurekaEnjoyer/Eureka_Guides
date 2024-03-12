# Haste

Author: Anna Molkot@Leviathan<br>
Last Updated: 11 March 2024

Questions or suggestions?<br>
Contact me here: [THL/#eureka-general-chat](https://discord.com/channels/578708223092326430/816800750147207199)


## Description

Haste is a bonus found on certain pieces of gear orignating from Eureka.  
Each point of haste directly reduces (as in, does not increase skill/speed speed) GCD as well as other cast and recast times by about 1%. 
Each piece of haste gear gives Haste +3 bonus, so each piece reduces these times by about 3%.

## Calculating GCDs

Exact calculation of GCDs with haste gear is simple.  In order to calculate this reduction, we will need to use a slightly edited version of the [Weaponskill and Spell Cast and Global Cooldown Reduction formula](https://www.akhmorning.com/allagan-studies/stats/speed/#formulae)
provided by Allagan Studies.  
Accounting for haste and plugging in specific level-70 modifiers gives us

$$t\left(t_0, n, s\right) = \frac{1}{100} \left \lfloor t_0 \left(1 - 0.01 n\right) \left(100 + \frac{1}{10} \left \lceil  \frac{130}{900} \left (  364 - s \right ) \right \rceil \right)\right\rfloor$$ where <br>
$t = t\left(t_0, n, s\right)$ 		is the reduced action (re)cast time, in seconds;<br>
$t_0$ 						is the action (re)cast time, absent any speed or haste gear (think 2.5 for GCD), in seconds;<br>
$n$ 						is the number of points of haste;<br>
$s$ 						is skill/spell speed substat amount;<br>
$\left \lfloor A \right \rfloor$ is the floor function applied onto $A$; and<br>
$\left \lceil A \right \rceil$ is the ceiling function applied onto $A$.

### Example:

Suppose I have 3 points of haste and a skill speed of 603, and I wish to determine my current GCD.  We use the above formula and the information given to solve below:<br>

$\text{GCD} = t\left(2.5, 3, 603\right) = 2.34$
