// write a console bmi application
// user will input weight and height
// weight in kilograms
// height in inches
// all logic should be in one function
// and calculate BMI and category

using System;
class Program
{
    static void Main(string[] args)
    {
        CalculateBMI();
    }

    static void CalculateBMI()
    {
        Console.Write("Enter your weight in kilograms: ");
        double weight = double.Parse(Console.ReadLine());
        Console.Write("Enter your height in inches: ");
        double height = double.Parse(Console.ReadLine());
        double heightInMeters = height * 0.0254;
        double bmi = weight / (heightInMeters * heightInMeters);
        string category;
        if (bmi < 18.5)
        {
            category = "Underweight";
        }
        else if (bmi < 24)
        {
            category = "Healthy weight";
        }
        else if (bmi < 27)
        {
            category = "Overweight";
        }
        else
        {
            category = "Obesity";
        }
        Console.WriteLine($"Your BMI is {bmi:F2} and you are categorized as {category}.");
    }
}