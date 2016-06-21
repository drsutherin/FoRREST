using System;
using System.Diagnostics;
using System.Collections.Generic;
using System.Collections;


namespace euler {
    class Problem38 {
        
        public static void Main(string[] args) {
            new Problem38().BruteForce();            
        }

        public void BruteForce() {
            Stopwatch clock = Stopwatch.StartNew();

            long result = 0;
            for (long i = 9387; i >= 9234; i--) {
                result = concat(i, 2*i);
                if(isPandigital(result)){                    
                    break;
                }
            }
            
            clock.Stop();
            Console.WriteLine("The largest pandigital product is {0}", result);
            Console.WriteLine("Solution took {0} ms", clock.ElapsedMilliseconds);
        }


        private long concat(long a, long b) {
            long c = b;
            while (c > 0) {
                a *= 10;
                c /= 10;
            }
            return a + b;
        }

        private bool isPandigital(long n) {
            int digits = 0;
            int count = 0;
            int tmp;

            while (n > 0) {
                tmp = digits;
                digits = digits | 1 << (int)((n % 10) - 1); //The minus one is there to make 1 fill the first bit and so on
                if (tmp == digits) { //Check to see if the same digit is found multiple times
                    return false;
                }

                count++;
                n /= 10;
            }

            return digits == (1 << count) - 1;
        }

    }
}

