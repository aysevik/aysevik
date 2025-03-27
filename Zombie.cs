using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Heroic
{
	public class Zombie : GameCharacter
	{
		public int Strength { get; }

		public Zombie(string name, int strength, int maxHealthPoints = 100)
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
			return randomNumberGenerator.Next(Strength / 2, Strength + 1);
		}
	}
}
