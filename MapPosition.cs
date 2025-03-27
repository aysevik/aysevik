using System;
using System.Security.Cryptography.X509Certificates;

namespace Heroic
{
	public class MapPosition
	{
		public static MapPosition Zero { get; } = new MapPosition(0, 0);
		public int X { get; }
		public int Y { get; }

		public MapPosition(int x, int y)
		{
			X = x;
			Y = y;
		}


		public MapPosition Translate(int deltaX, int deltaY)
		{
			return new MapPosition(X + deltaX, Y + deltaY);
		}

		public override string ToString()
		{
			return $"(X={X}, Y={Y})";
		}

		public override bool Equals(object obj)
		{
			return obj is MapPosition position &&
				   X == position.X &&
				   Y == position.Y;
		}

		public override int GetHashCode()
		{
			return X.GetHashCode() * 11 + 13 * Y.GetHashCode();
		}


	}
}
