using backend.Application.Interfaces;
using backend.Domain.Entities;

namespace backend.Infrastructure.Services
{
    public class MockAccountService : IAccountService
    {
        public Task<Account> GetAccountAsync(int accountId)
        {
            var account = new Account
            {
                AccountId = accountId,
                Balance = 10000M,
                Transactions = new List<Transaction>
                {
                    new Transaction
                    {
                        TransactionId = 1,
                        Date = DateTime.Now.AddDays(-5),
                        Description = "Depósito",
                        Amount = 5000M,
                        BalanceAfter = 10000M
                    },
                    new Transaction
                    {
                        TransactionId = 2,
                        Date = DateTime.Now.AddDays(-3),
                        Description = "Transferência",
                        Amount = -2000M,
                        BalanceAfter = 8000M
                    }
                }
            };
            return Task.FromResult(account);
        }

        public Task<decimal> GetBalanceAsync(int accountId)
        {
            // Return mock balance
            return Task.FromResult(8000M);
        }

        public Task<List<Transaction>> GetTransactionHistoryAsync(int accountId)
        {
            // Return mock transactions
            var transactions = new List<Transaction>
            {
                new Transaction
                {
                    TransactionId = 1,
                    Date = DateTime.Now.AddDays(-5),
                    Description = "Depósito",
                    Amount = 5000M,
                    BalanceAfter = 10000M
                },
                new Transaction
                {
                    TransactionId = 2,
                    Date = DateTime.Now.AddDays(-3),
                    Description = "Transferência",
                    Amount = -2000M,
                    BalanceAfter = 8000M
                }
            };
            return Task.FromResult(transactions);
        }

        public Task<bool> BuyCurrencyAsync(int accountId, string currencyFrom, string currencyTo, decimal amount)
        {
            // Mock buying currency - simply return true
            return Task.FromResult(true);
        }
    }
}