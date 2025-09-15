namespace backend.Domain.Entities
{
    public class Account
    {
        public int AccountId { get; set; }
        public decimal Balance { get; set; }
        public List<Transaction> Transactions { get; set; }
    }
}