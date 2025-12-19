using System;

namespace helloApp{

    public class Code{
        
        // int i=0;
            // while(i > 0){
            //     Console.WriteLine($"The number is : {i}");
            //     i -= 1;
            // }

            // do{
            //     Console.WriteLine($"The number is : {i}");
            //     i += 1;
            // }while(i <= 10);

            // for(int j= 0 ; j < 12;j++){
            //     Console.WriteLine($"The number is : {j}");
            // }

            // for(int j= 10 ; j>0;j--){
            //     Console.WriteLine($"The number is : {j}");
            // }

            // int[] arr = {1,2,3,4,5,6};
            // foreach(var j in arr){
                
            //     Console.WriteLine($"The number is : {j}");
            // }

            // for(int j=0;j<arr.Length;j++){
            //     Console.WriteLine($"The number at index {j} is  : {arr[j]}");
            // }

            // while (i < arr.Length){
            //     Console.WriteLine($"The number at index {i} is  : {arr[i]}");
            //     i++;
            // }
        public void f1(){
            Console.WriteLine("To print n numbers.");
            int n = 0;
            Console.WriteLine("Enter n: ");
            n = int.Parse(Console.ReadLine());

            for(int i=1;i<=n;i++){
                Console.WriteLine($"{i}");
            }

        }

        public void f2(){
            Console.WriteLine("To print even numbers.");
            
            for(int i=1;i<=10;i++){
                if (i%2 == 0){
                    Console.WriteLine($"{i}");
                }
            }

        }

        public void f3(){
            Console.WriteLine("To print sum first natural n numbers.");
            int n = 0;
            Console.WriteLine("Enter n: ");
            n = int.Parse(Console.ReadLine());
            int res = 0;
            for(int i=1;i<=n;i++){
                res += i;
            }
            Console.WriteLine($"the sum of first n natural number is: {res} ");

        }

        public void f4(){
            Console.WriteLine("To print mutiplication table.");
            int n = 0;
            Console.WriteLine("Enter n: ");
            n = int.Parse(Console.ReadLine());

            for(int i=1;i<=10;i++){
                Console.WriteLine($"n X {i} = {n*i}");
            }

        }

         public void f5(){
            Console.WriteLine("To power of a  numbers.");
            int n = 0;
            Console.WriteLine("Enter n: ");
            n = int.Parse(Console.ReadLine());
            int b = 0;
            Console.WriteLine("Enter b: ");
            b = int.Parse(Console.ReadLine());
            int res = 1;
            for(int i=1;i<=b;i++){
                res *= n;
            }
            Console.WriteLine($"{n} to the power {b} is: {res} ");

        }

        public void f6(){
            Console.WriteLine("To find the n fibbonacci  numbers.");
            int n = 0;
            Console.WriteLine("Enter n: ");
            n = int.Parse(Console.ReadLine());
            int a = 0;
            int b = 1;
            Console.WriteLine($"{a} ");
            for(int i=0;i<n-1;i++){
                Console.WriteLine($"{a+b}");
                int t = a;
                a = b;
                b = t+b;
            }
            

        }

        public void f7(){
            Console.WriteLine("To check if it armstrong or not.");
            int n = 0;
            Console.WriteLine("Enter n: ");
            n = int.Parse(Console.ReadLine());

            int a = n;
            int res = 0;
            while (a > 0){
                int d = a % 10;
                res += d * d * d;
                a /= 10;
            }
            if (res == n){
                Console.WriteLine($"{n} is a armstrong number.");
            }
            else{
                Console.WriteLine($"{n} is a armstrong number.");
            }

        }

        public void f8(){
            Console.WriteLine("To check if it armstrong or not.");
            int n1 = 0;
            Console.WriteLine("Enter n1: ");
            n1 = int.Parse(Console.ReadLine());

            int n2 = 0;
            Console.WriteLine("Enter n1: ");
            n2 = int.Parse(Console.ReadLine());
            for(int i=n1;i<=n2;i++){
                int a = i;
                int res = 0;
                while (a > 0){
                    int d = a % 10;
                    res += d * d * d;
                    a /= 10;
                }
                if (res == i){
                    Console.WriteLine($"{i} is a armstrong number.");
                }
                else{
                    Console.WriteLine($"{i} is a armstrong number.");
                }
            }

        }

        public void f9(){
            Console.WriteLine("To check wheater a number is prime or not.");
            int n = 0;
            Console.WriteLine("Enter n: ");
            n = int.Parse(Console.ReadLine());
            
            if (n < 2){
                Console.WriteLine($"{n} is not a prime number.");
            }
            int f = 1;

            
            for(int i=2; i<=Math.Sqrt(n);i++){
                if (n%i == 0){
                    f = 0;

                    break;
                }
            }
            if (f== 1){
                Console.WriteLine($"{n} is a prime number.");
            }
            else{
                Console.WriteLine($"{n} is not a prime number.");
            }
            

        }

        public void f10(){
            Console.WriteLine("To find odd number in given range ");
            int n1 = 0;
            Console.WriteLine("Enter n1: ");
            n1 = int.Parse(Console.ReadLine());

            int n2 = 0;
            Console.WriteLine("Enter n1: ");
            n2 = int.Parse(Console.ReadLine());
            if(n1 % 2 == 0)
            {
                n1++;
            }

            for(int i=n1;i<=n2;i+=2){
                Console.WriteLine(i);
            }

        }

        public void f11(){
            Console.WriteLine("To find multiple of 3 and 5 in a give range ");
            int n1 = 0;
            Console.WriteLine("Enter n1: ");
            n1 = int.Parse(Console.ReadLine());

            int n2 = 0;
            Console.WriteLine("Enter n1: ");
            n2 = int.Parse(Console.ReadLine());
            
            int res = 0;

            for(int i=n1;i<=n2;i+=2){
                if(i % 3 == 0 || i % 5 == 0){
                    Console.WriteLine(i);
                    res += i;
                }
            }

            Console.WriteLine($"Sum of all mutiple of 3 and 5 in range {n1} to {n2} is : {res}");

        }

        public void f12(){
            Console.WriteLine("To find multiple of 17 in a give range ");
            int n1 = 0;
            Console.WriteLine("Enter n1: ");
            n1 = int.Parse(Console.ReadLine());

            int n2 = 0;
            Console.WriteLine("Enter n1: ");
            n2 = int.Parse(Console.ReadLine());
            
            

            for(int i=n1;i<=n2;i+=2){
                if(i % 17 == 0){
                    Console.WriteLine(i);
        
                }
            }

        }


        public void f13(){
            Console.WriteLine("To find sum of digits of a number ");
            int n1 = 0;
            Console.Write("Enter a Number: ");
            n1 = int.Parse(Console.ReadLine());

            int res = 0;
            while (n1 > 0){
                res += n1 % 10;
                n1 /= 10;
            }

            Console.WriteLine($"\nSum of Digits of the Number: {res}");

        }

        public void f14()
        {
            Console.WriteLine("To print pyrammid of numbers "); 
            int rows = 5;
            for (int i = 1; i <= rows; i++)
            {
                for (int space = 1; space <= rows - i; space++)
                {
                    Console.Write(" ");
                }

                for (int j = 1; j <= i; j++)
                {
                    Console.Write(j + " ");
                }

                Console.WriteLine();
            }
        }


        public void f15()
        {
            Console.WriteLine("To print pyrammid ");   
            for(int i = 1; i <= 5; i++)
            {
                for(int j = 0; j < 5 - i; j++)
                {
                    Console.Write(" ");
                }
                for(int j =1;j<= i; j++)
                {
                    Console.Write("*" + " ");
                }
                Console.Write("\n");
            }
        }

        






        




        
    }
}



//     1
//    1 2
//   1 2 3
//  1 2 3 4
// 1 2 3 4 5
