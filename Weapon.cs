using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Heroic;

public class Weapon
{
	public string Name { get; }
	public int DamagePoints { get; }
	public WeaponRange Range { get; }

	public Weapon(string name, int damagePoints, WeaponRange range)
	{
		Name = name;
		DamagePoints = damagePoints;
		Range = range;
	}

}
