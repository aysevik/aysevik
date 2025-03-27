using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;

namespace Heroic
{
	public class Barbarian : GameCharacter
	{

		public Weapon Weapon { get; private set; }

		public Barbarian(string name, int maxHealthPoints, Weapon weapon = null)
		{
			Name = name;
			MaxHealthPoints = maxHealthPoints;
			HealthPoints = MaxHealthPoints;
			Weapon = weapon;
		}

		public override bool CanAttack { get { return base.CanAttack && Weapon != null; } }
		public override bool CanDie { get { return base.CanDie; } }
		public override bool CanMove { get { return base.CanMove; } }

		public void DropWeapon()
		{
			if (Weapon != null)
			{
				Console.WriteLine($"{Name} drops {Weapon.Name}.");
				Weapon = null;
			}
			else
			{
				Console.WriteLine($"{Name} has no weapon to drop.");
			}
		}

		public void PickUpWeapon(Weapon newWeapon)
		{
			if (newWeapon != null)
			{
				Console.WriteLine($"{Name} picks up {newWeapon.Name}.");
				Weapon = newWeapon;
			}
			else
			{
				Console.WriteLine($"{Name} cannot pick up a null weapon.");
			}
		}


		protected override int CalculateDamage(GameCharacter target)
		{
			if (Weapon != null)
			{
				return randomNumberGenerator.Next(Weapon.DamagePoints / 2, Weapon.DamagePoints + 1);
			}
			else
			{
				// Default damage if no weapon is equipped
				return randomNumberGenerator.Next(10, 21);
			}
		}
	}
}