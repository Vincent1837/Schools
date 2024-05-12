var Animal = {name: "Animal"};
Animal.hello = function() {
    console.log(this.name + " say hello");
};

var Bird = Object.create(Animal);
Bird.name = "Bird";
Bird.fly = function(where) {
    console.log(this.name + " fly " + where);
};

// Create object Penguin
var Penguin = Object.create(Bird);
Penguin.name = "Penguin";
Penguin.fly = function(where) {
    console.log(this.name + " can't fly");
};

// Create object Duck
var Duck = Object.create(Bird);
Duck.name = "Duck";
Duck.quack = function() {
    console.log(this.name + ": quack!");
};

// Create function forcedToFly
function forcedToFly(entity) {
    Bird.fly.call(entity, "in the sky");
}

// Please keep the following test cases
console.log("0.")
Animal.hello()
Bird.hello()
Bird.fly("in the sky")

console.log("1.")
Penguin.hello()
Penguin.fly("in the sky")

console.log("2.")
Duck.hello()
Duck.fly("in the sky")
Duck.quack()

console.log("3.")
forcedToFly(Animal)
forcedToFly(Penguin)

/*
0.
Animal say hello
Bird say hello
Bird fly in the sky
1.
Penguin say hello
Penguin can't fly
2.
Duck say hello
Duck fly in the sky
Duck: quack!
3.
Animal fly in the sky
Penguin fly in the sky
*/