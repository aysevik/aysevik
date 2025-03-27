using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Heroic
{
	public abstract class GameCharacter
	{
		protected static readonly Random randomNumberGenerator = new Random();
		private int healthPoints;
		private MapPosition position;
		private bool trace = false;


		public virtual bool CanAttack { get { return IsAlive; } }

		public virtual bool CanDie { get { return IsAlive; } }

		public virtual bool CanMove { get { return IsAlive; } }

		public int HealthPoints
		{
			get { return healthPoints; }
			protected set { healthPoints = value; }
		}

		public bool IsAlive => healthPoints > 0;

		public bool IsDead => !IsAlive;

		public int MaxHealthPoints { get; protected set; }

		public string Name { get; protected set; }

		public MapPosition Position
		{
			get { return position; }
			set { position = value; }
		}

		public bool Trace
		{
			get { return trace; }
			set { trace = value; }
		}

		public virtual void Attack(GameCharacter target)
		{
			if (CanAttack && target != null && target.CanDie)
			{
				int damage = CalculateDamage(target);
				target.HealthPoints -= damage;
				Console.WriteLine($"{Name}is attacking {target.Name} and deals {damage} points of damage.");
			}
			else
			{
				Console.WriteLine($"{Name} can not attack");
			}
		}

		protected virtual int CalculateDamage(GameCharacter target)
		{

			return 0;
		}

		public void Heal(int amount)
		{
			if (IsAlive)
			{
				healthPoints = Math.Min(MaxHealthPoints, healthPoints + amount);
				if (Trace)
				{
					Console.WriteLine($"{Name} is healed by {amount} points. Current health: {HealthPoints}");
				}
			}
		}

		public void Kill()
		{
			healthPoints = 0;
		}

		public void MoveBy(int deltaX, int deltaY)
		{
			Position = Position.Translate(deltaX, deltaY);
			if (Trace)
			{
				Console.WriteLine($"{Name} moved to {Position}");
			}
		}

		public void MoveTo(MapPosition newPosition)
		{
			Position = newPosition;
			if (Trace)
			{
				Console.WriteLine($"{Name} moved to {Position}");
			}
		}




	}
}
