using System;
using System.Collections.Generic;
using System.Linq;

namespace Heroic
{
	class Game
	{
		private static readonly Random randomNumberGenerator = new Random();

		static void Main(string[] args)
		{
			Weapon axe = new Weapon("Golden Axe", 50, WeaponRange.Close);
			Weapon sword = new Weapon("Sword of Heaven", 70, WeaponRange.Close);
			Weapon bow = new Weapon("Bow of Evil", 30, WeaponRange.Long);

			Barbarian giant = new("The Giant", 175);
			Barbarian goliath = new("Goliath", 200, weapon: sword);
			Barbarian bigBaby = new("Big Baby", 250, weapon: null);

			Dwarf gandalf = new("Gandalf", 50);
			Dwarf pinky = new("Pinky", strength: 2);
			Zombie nemesis = new("Nemesis", strength: 20);



			List<GameCharacter> characters = new List<GameCharacter> { giant, goliath, gandalf, pinky, nemesis, bigBaby };
			foreach (var character in characters)
			{
				Console.WriteLine($"The {character.GetType().Name.ToLower()} {character.Name} was born!");
			}
			giant.PickUpWeapon(axe);
			goliath.PickUpWeapon(bow);
			goliath.PickUpWeapon(sword);

			PlaceCharacters(characters);
			Brawl(characters);
			ShowFinalStatus(characters);
		}

		static void PlaceCharacters(List<GameCharacter> characters)
		{
			foreach (GameCharacter aCharacter in characters)
			{
				aCharacter.Position = new MapPosition(0, 0);
				aCharacter.MoveBy(randomNumberGenerator.Next(100), randomNumberGenerator.Next(100));
			}
		}

		static void Brawl(List<GameCharacter> characters)
		{
			int round = 0;
			while (round < 10 && characters.Count > 1)
			{
				round++;
				Console.WriteLine($"\nRound {round} begins...");
				Console.WriteLine(string.Join(" | ", characters.Select(c => $"{c.Name}: {c.HealthPoints}")));

				GameCharacter[] remainingCharacters = characters.ToArray();
				randomNumberGenerator.Shuffle(remainingCharacters);

				GameCharacter attacker = remainingCharacters[0];
				GameCharacter defender = remainingCharacters[1];
				attacker.Attack(defender);

				if (attacker.IsDead) characters.Remove(attacker);
				if (defender.IsDead) characters.Remove(defender);

				if (randomNumberGenerator.NextDouble() > 0.9)
				{
					Console.WriteLine("A wonder happened...");
					int randomIndex = randomNumberGenerator.Next(characters.Count);
					int healingPoints = randomNumberGenerator.Next(50);
					characters[randomIndex].Heal(healingPoints);
				}
			}

		}

		static void ShowFinalStatus(List<GameCharacter> characters)
		{
			Console.WriteLine("\nFinal character status :");
			foreach (var character in characters)
			{
				Console.WriteLine($"{character.Name}: {character.HealthPoints} | ");
			}

			GameCharacter winner = characters.OrderByDescending(c => c.HealthPoints).FirstOrDefault();
			Console.WriteLine($"The winner is {winner.Name}");
		}
	}
}

