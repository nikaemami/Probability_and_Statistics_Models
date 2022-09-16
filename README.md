# Probability_and_Statistics_Models
Implementation of different basic probability and statistics models.

<h2>Poisson Distribution</h2>

Implementing a Poisson distribution for the number of people riding a bus. Consider that number of people who get on a bus comes from a Poisson distribution, and that 3 people get on a bus per minute on average. Estimate the distribution for a timeline of a 100 days.

The distribution was estimated using the Numpy library as below:

```ruby
x_poisson=np.random.poisson(lam = 3,size = 1000)
    x_avg=sum(x_poisson)/1000
```

The result is as follows:

![My Image](images/3.png)

<h2>Independant Uniform Distributions</h2>

Assuming that X, Y are independant and come from a distribution of U[0,1], the following expressions were computed:

<img src="images/4.png" width="146" height="26.5">

```ruby
if( X**2 + Y**3 > 0.75 ):
        n+=1
```

<img src="images/5.png" width="146" height="26.5">

```ruby
if( X + Y > 5 * X  * (Y**(0.5))):
        n+=1
```

<img src="images/6.png" width="89" height="39">

Monte Carlo:

```ruby
for i in range (1000):
    Xn=np.random.uniform(-1,1)
    sum+=f(Xn)
    y.append((b-a)*sum/(i+1))
```

Result:

![My Image](images/9.png)

<img src="images/7.png" width="75.5" height="35.5">

Monte Carlo:

```ruby
for i in range (1000):
    Xn=np.random.uniform(0,1)
    sum+=f(Xn)
    y.append((b-a)*sum/(i+1))
```

Result:

![My Image](images/10.png)

<img src="images/8.png" width="76" height="34">

Monte Carlo:

```ruby
for i in range (5000):
    Xn=np.random.uniform(0,3)
    sum+=f(Xn)
    y.append((b-a)*sum/(i+1))
```

Result:

![My Image](images/11.png)

<h2>Normal and Exponential Distribution</h2>

These two distributions were implemented by using the **inverse of the cumulative distribution** and the **uniform distribution**:

Exponential:

```ruby
def exp_inverse(Fx):
    x=-np.log(1-Fx)
    return x
    
for i in range (100):
    Fx=np.random.uniform(0,1)
    x_exp=exp_inverse(Fx)
```

![My Image](images/12.png)

Normal:

```ruby
def norm_inverse(Fx):
    from scipy.stats import norm
    x=norm.ppf(Fx)
    return x

for i in range (100):
    Fx=np.random.uniform(0,1)
    x_norm=norm_inverse(Fx)
```

![My Image](images/13.png)

<h2>Correlation Coefficient:</h2>

Using Mesh in MATLAB, the following graphs are for **normal distributions** with means of 0, and stds and correlation coeeficients as below:

<img src="images/14.png" width="233" height="41">

```
normal_distribution=n(0,1,1,x,y);
surf(x,y,normal_distribution)
```

<img src="images/15.png" width="210" height="170">

<img src="images/26.png" width="261.5" height="194.5">

<img src="images/16.png" width="244" height="38">

```
normal_distribution=n(0.8,1,1,x,y);
surf(x,y,normal_distribution)
```

<img src="images/17.png" width="210" height="170">

<img src="images/27.png" width="261.5" height="194.5">

<img src="images/18.png" width="262" height="38">

```
normal_distribution=n(-0.8,1,1,x,y);
surf(x,y,normal_distribution)
```

<img src="images/19.png" width="210" height="170">

<img src="images/28.png" width="261.5" height="194.5">

<img src="images/20.png" width="222" height="33">

```
normal_distribution=n(0,1,2,x,y);
surf(x,y,normal_distribution)
```

<img src="images/21.png" width="210" height="170">

<img src="images/29.png" width="261.5" height="194.5">

<img src="images/22.png" width="241" height="38">

```
normal_distribution=n(0.8,1,2,x,y);
surf(x,y,normal_distribution)
```

<img src="images/23.png" width="210" height="170">

<img src="images/30.png" width="261.5" height="194.5">

<img src="images/24.png" width="246" height="39">

```
normal_distribution=n(0.8,1,5,x,y);
surf(x,y,normal_distribution)
```

<img src="images/25.png" width="210" height="170">

<img src="images/31.png" width="261.5" height="194.5">

<h2>Estimation of Pi:</h2>

By generating random points for (x,y) in a uniform distribution inside a square of 1x1, the goal is to find the points which fall into the circle with area of Pi. The model is like this:

<img src="images/32.png" width="373" height="273">

Implementation of the problem above with total number of generated points equal to 100, 1000, 10000, 100000:

```ruby
def estimation(n):
    in_circle=0
    for i in range (n):
        x=np.random.uniform(0,2)
        y=np.random.uniform(0,2)
        if((((x-1)**2+(y-1)**2)**(0.5))<1):
            in_circle+=1
    return (float(in_circle/n))
```

The results are as below:

```
number of points = 100
Pi = 3.16
accuracy = 0.005859240340778607

number of points = 1000
Pi = 3.128
accuracy = 0.0043266760171027045

number of points = 10000
Pi = 3.1308
accuracy = 0.0034354083357881885

number of points = 100000
Pi = 3.1462
accuracy = 0.0014665639114422135
```

<h2>Heights of people in a class</h2>

A total number of k people are in a class. Their heights varies between 1 to 320, and only consists integer values. What value should k have, so that two people have the same height with the probability of p = 0.5?

The problem was solved both by using the mathematical formula and the python libraries, and the results where the same, and as follows:

The mathematical view:

```ruby
i = 1
while (i < 60):
    probability.append(1-(math.factorial(320)/((math.factorial(320-(i+1)))*(320**(i+1)))))
    i=i+1
```

Result:

![My Image](images/1.png)

The programming view:

```ruby
or i in range(59):
    favorable=0
    for j in range(99):
        classes=[]
        for k in range (i+2):
            classes.append(random.randint(1,320))
        classes.sort()
        for k in range (i+1):
            if(classes[k]==classes[k+1]):
                favorable+=1
                break       
    probability.append(favorable/100)
```

Result:

![My Image](images/2.png)
