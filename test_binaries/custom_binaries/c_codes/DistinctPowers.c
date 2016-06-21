using System;   
using System.Diagnostics;
using System.Collections.Generic;


namespace euler {
    class Problem29 {

        public static void Main(string[] args) {
            new Problem29().BruteForce();
            new Problem29().BruteForceSortedSet();
        }

        public void BruteForce() {
            Stopwatch clock = Stopwatch.StartNew();

            List<double> set = new List<double>();

            for (int a = 2; a <= 100; a++) {
                for (int b = 2; b <= 100; b++) {
                    double result = Math.Pow(a, b);
                    if (!set.Contains(result)) {
                        set.Add(result);
                    }
                }
            }
                        
            clock.Stop();            
            Console.WriteLine("The number of distinct terms are {0}", set.Count);
            Console.WriteLine("Solution took {0} ms", clock.ElapsedMilliseconds);
        }

        public void BruteForceSortedSet() {
            Stopwatch clock = Stopwatch.StartNew();

            SortedSet<double> set = new SortedSet<double>();
            
            for (int a = 2; a <= 100; a++) {
                for (int b = 2; b <= 100; b++) {
                    double result = Math.Pow(a, b);                    
                        set.Add(result);                    
                }
            }

            clock.Stop();
            Console.WriteLine("The number of distinct terms are {0}", set.Count);
            Console.WriteLine("Solution took {0} ms", clock.ElapsedMilliseconds);
        }

    }
}

