using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Heroic
{
	public class Dwarf : GameCharacter
	{
		public int Strength { get; }

		public Dwarf(string name, int strength, int maxHealthPoints = 100)
		{
			Name = name;
			MaxHealthPoints = maxHealthPoints;
			HealthPoints = MaxHealthPoints;
			Strength = strength;
		}

		public override bool CanAttack => true;
		public override bool CanDie => true;
		public override bool CanMove => true;



		protected override int CalculateDamage(GameCharacter target)
		{
			if (target is Barbarian)
			{
				return randomNumberGenerator.Next(Strength / 2, Strength + 1) * 2;
			}
			else if (target is Dwarf)
			{
				return randomNumberGenerator.Next(Strength / 2, Strength + 1) * 5;
			}
			else
			{
				return randomNumberGenerator.Next(Strength / 2, Strength + 1);
			}
		}
	}
}

