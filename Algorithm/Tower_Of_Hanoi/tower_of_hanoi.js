const tower_of_hanoi = (n, from_rod, to_rod, using_rod) => {
    if (n === 1) {
        console.log(`Move disk 1 from ${from_rod} to ${to_rod}`);
        return;
    }
    tower_of_hanoi(n - 1, from_rod, using_rod, to_rod);
    console.log(`Move disk ${n} from ${from_rod} to ${to_rod}`);
    tower_of_hanoi(n - 1, using_rod, to_rod, from_rod);
};

tower_of_hanoi(5, "A", "C", "B");